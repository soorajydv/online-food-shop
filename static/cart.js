// cart.js
function addToCart(foodItemId) {
    // Send an AJAX request to the server to add the item to the cart
    $.ajax({
      url: '/add_to_cart/',
      method: 'POST',
      data: {
        food_item_id: foodItemId,
        csrfmiddlewaretoken: '{{ csrf_token }}'
      },
      success: function(response) {
        // Handle the response as needed (e.g., show a success message)
      },
      error: function(xhr, status, error) {
        // Handle errors if any
      }
    });
  }
  