$('#slider1, #slider2, #slider3, #slider4, #slider5').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 5,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})

//quanty , remove item

// Handle the "Plus Cart" button click
$('.plus-cart').click(function () {
    var id = $(this).attr('pid').toString(); // Get the product ID
    var eml = $(this).closest('div').find('#quantity'); // Find the quantity element
    $.ajax({
        type: "GET",
        url: "/pluscart", // Your Django URL to handle the request
        data: {
            prod_id: id // Send product ID to the server
        },
        success: function (data) {
            eml.text(data.quantity); // Update the quantity dynamically
            document.getElementById("amount").innerText = (data.amount);
            document.getElementById("totalamount").innerText = (data.totalamount);
        },
        error: function (xhr, status, error) {
            console.error("Error: ", error); // Handle errors
        }
    });
});

// Handle the "Minus Cart" button click
$('.minus-cart').click(function () {
    var id = $(this).attr('pid').toString(); // Get the product ID
    var eml = $(this).closest('div').find('#quantity'); // Find the quantity element
    $.ajax({
        type: "GET",
        url: "/minuscart", // Your Django URL to handle the request
        data: {
            prod_id: id // Send product ID to the server
        },
        success: function (data) {
            eml.text(data.quantity); // Update the quantity dynamically
            document.getElementById("amount").innerText = (data.amount);
            document.getElementById("totalamount").innerText = (data.totalamount);
        },
        error: function (xhr, status, error) {
            console.error("Error: ", error); // Handle errors
        }
    });
});

/// Handle the "Remove Item" button click
$('.remove-cart').click(function () {
    var id = $(this).attr('pid').toString(); // Get the product ID
    var eml = this
    
    $.ajax({
        type: "GET",
        url: "/removecart", // Your Django URL to handle the request
        data: {
            prod_id: id // Send product ID to the server
        },
        success: function (data) {
                document.getElementById("amount").innerText = data.amount 
                document.getElementById("totalamount").innerText = data.totalamount
                eml.parentNode.parentNode.parentNode.parentNode.remove()
            },

        error: function (xhr, status, error) {
            console.error("Error: ", error); // Handle errors
        }
    });
});


