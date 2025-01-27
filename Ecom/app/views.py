from django.shortcuts import render,redirect
from django.views import View
from .models import *
from .forms import CustomerRegisterationForm,CustomerProfileForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class ProductView(View):
    def get(self,request):
        totalitem = 0
        banners = Banner.objects.all()
        live_sale = LiveSale.objects.first()
        topwears = Product.objects.filter(category='top wear')
        bottomwears = Product.objects.filter(category='bottom wear')
        mobiles = Product.objects.filter(category='mobile')
        glasses = Product.objects.filter(category='glasses')
        electronics = Product.objects.filter(category='electronics')
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        context = {'topwears':topwears, 'bottomwears':bottomwears, 'mobiles':mobiles, 'glasses':glasses, 'electronics':electronics, 'totalitem':totalitem , 'banners': banners,'live_sale': live_sale}
        return render(request, 'app/home.html', context)

class ProductDetailView(View):
    def get(self,request,pk):
        totalitem = 0
        product = Product.objects.get(pk=pk)
        item_already_in_cart = False
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            item_already_in_cart = Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
        context = {'product':product, 'item_already_in_cart':item_already_in_cart, 'totalitem':totalitem}
        return render(request, 'app/productdetail.html',context)

@login_required
def add_to_cart(request):
    user=request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id = product_id)
    cart = Cart(user=user, product=product)
    cart.save()
    return redirect('/showcart')

@login_required
def show_cart(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        user = request.user
        cart = Cart.objects.filter(user=user)
        # print(cart)
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        # print(cart_product)
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.discount_price) #quantity multiply price
                amount += tempamount # add all tempamount
                totalamount = amount +shipping_amount 
            return render(request, 'app/addtocart.html', {'carts':cart, 'totalamount': totalamount, 'amount':amount, 'totalitem':totalitem})
        else:
            return render(request, 'app/emptycart.html')
        
@login_required       
def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')  # Safely get the product ID from the request
        try:
            # Get the cart item for the user and the specified product
            cart_item = Cart.objects.get(Q(product_id=prod_id) & Q(user=request.user))
            cart_item.quantity += 1
            cart_item.save()

            # Calculate the amounts
            amount = 0.0
            shipping_amount = 70.0
            cart_products = Cart.objects.filter(user=request.user)  # Fetch all cart items for the user

            for item in cart_products:
                temp_amount = item.quantity * item.product.discount_price  # Multiply quantity by discount price
                amount += temp_amount  # Sum up all item amounts

            total_amount = amount + shipping_amount

            # Prepare response data
            data = {
                'quantity': cart_item.quantity,
                'amount': amount,
                'totalamount': total_amount
            }
            return JsonResponse(data)

        except Cart.DoesNotExist:
            return JsonResponse({'error': 'Cart item does not exist'}, status=404)
        except Product.DoesNotExist:
            return JsonResponse({'error': 'Product does not exist'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

@login_required    
def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')  # Safely get the product ID from the request
        try:
            # Get the cart item for the user and the specified product
            cart_item = Cart.objects.get(Q(product_id=prod_id) & Q(user=request.user))
            
            # Decrease the quantity, ensuring it doesn't go below 1
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
            else:
                cart_item.delete()  # Remove the item from the cart if the quantity reaches 0

            # Calculate the amounts
            amount = 0.0
            shipping_amount = 70.0
            cart_products = Cart.objects.filter(user=request.user)  # Fetch all cart items for the user

            for item in cart_products:
                temp_amount = item.quantity * item.product.discount_price  # Multiply quantity by discount price
                amount += temp_amount  # Sum up all item amounts

            total_amount = amount + shipping_amount

            # Prepare response data
            data = {
                'quantity': cart_item.quantity if cart_item.quantity > 0 else 0,
                'amount': amount,
                'totalamount': total_amount,
            }
            return JsonResponse(data)

        except Cart.DoesNotExist:
            return JsonResponse({'error': 'Cart item does not exist'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
    
@login_required
def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')  # Safely get the product ID from the request
        cart_item = Cart.objects.get(Q(product_id=prod_id) & Q(user=request.user))
        cart_item.delete()  
        amount = 0.0
        shipping_amount = 70.0
        cart_products = Cart.objects.filter(user=request.user)  # Fetch all cart items for the user
        for item in cart_products:
            temp_amount = item.quantity * item.product.discount_price  # Multiply quantity by discount price
            amount += temp_amount  # Sum up all item amounts

        # Prepare response data
        data = {
            'amount': amount,  
            'totalamount': amount + shipping_amount,   
            }
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

@login_required
def buy_now(request, product_id):
    product = Product.objects.get(id=product_id)
    
    # Check if the product is already in the cart. If not, add it.
    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product,
        defaults={'quantity': 1}  # Default quantity for the product if not already in the cart
    )
    
    # If the item was created (i.e., it's not already in the cart), save it
    if created:
        cart_item.save()
    
    # Redirect to the checkout page
    return redirect('checkout')  # Redirect to checkout page for this item


@login_required
def payment(request, order_id):
    order = OrderPlaced.objects.get(id=order_id, user=request.user)
    return render(request, 'app/payment.html', {'order': order})


@login_required
def address(request):
    totalitem = 0
    addrs = Customer.objects.filter(user=request.user)
    if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'app/address.html', {'address':addrs, 'active':'btn-primary', 'totalitem':totalitem})

@login_required
def orders(request):
    totalitem=0
    order_placed = OrderPlaced.objects.filter(user=request.user)
    if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'app/orders.html',{'order_placed': order_placed,'totalitem':totalitem})

@method_decorator(login_required,name='dispatch')
class ProfileView(View):
    def get(self,request):
        totalitem=0
        form = CustomerProfileForm
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        return render(request, 'app/profile.html',{'form':form, 'active':'btn-primary', 'totalitem':totalitem})
    def post(self,request):
        form =CustomerProfileForm(request.POST)
        if form.is_valid():
            userr = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=userr, name=name, locality=locality, city=city, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, 'Congratulation! Your Profile Updated Successfully')
        return render(request, 'app/profile.html', {'form':form, 'active':'btn-primary'})

@login_required
def mobile(request, data=None):
    if data is None:
        mobiles = Product.objects.filter(category='mobile')
    elif data in ['Huawmei', 'Sumsang', 'Vivo','iPhone','Nokia','Oppo']:
        mobiles = Product.objects.filter(category='mobile', brand=data)
    elif data in 'below':
        mobiles = Product.objects.filter(category='mobile', discount_price__lt=10000)
    elif data in 'above':
        mobiles = Product.objects.filter(category='mobile', discount_price__gt=10000)
    else:
        mobiles = Product.objects.filter(category='mobile')  # Handle unexpected data values gracefully

    totalitem=0
    if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
    context = {'mobiles': mobiles, 'data': data,'totalitem':totalitem}
    return render(request, 'app/mobile.html', context)

class CustomerRegisterationView(View):
    def get(self,request):
        form = CustomerRegisterationForm()
        return render(request, 'app/customerregistration.html', {'form':form})
    def post(self,request):
        form = CustomerRegisterationForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulations!! Registration Successfully Completed')
            form.save()
        return render(request, 'app/customerregistration.html', {'form':form})

@login_required
def checkout(request):
    totalitem = 0
    user=request.user
    address = Customer.objects.filter(user=user)
    cart_items = Cart.objects.filter(user=user)
    amount = 0.0
    shipping_amount =70.0
    total_amount = 0.0

    cart_products = Cart.objects.filter(user=request.user)
    if cart_products:
        for item in cart_products:
            temp_amount = item.quantity * item.product.discount_price  # Multiply quantity by discount price
            amount += temp_amount  # Sum up all item amounts
        total_amount = amount + shipping_amount

    if not address.exists():
        return redirect('profile') 
    
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'app/checkout.html', {'address':address, 'totalamount':total_amount, 'cartitems': cart_items, 'totalitem':totalitem})

@login_required
def payment_done(request):
    user=request.user
    custid = request.GET.get('custid')
    customer = Customer.objects.get(id=custid)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user, customer=customer, product=c.product, quantity=c.quantity).save()
        c.delete()
    return redirect('orders')

@login_required
def remove_address(request, address_id):
    # Fetch the address belonging to the logged-in user
    address =  Customer.objects.get(id=address_id, user=request.user)
    address.delete()  # Delete the address
    return redirect('address') 