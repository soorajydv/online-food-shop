// checkout.js
function checkout() {
    // Send an AJAX request to the server to create a PaymentIntent
    $.ajax({
      url: '/checkout/',
      method: 'POST',
      data: {
        csrfmiddlewaretoken: '{{ csrf_token }}'
      },
      success: function(response) {
        // Use the response.client_secret to complete the payment on the frontend
        const stripe = Stripe('YOUR_STRIPE_PUBLIC_KEY');
        stripe.confirmCardPayment(response.client_secret, {
          payment_method: {
            card: cardElement, // Example card element
            billing_details: {
              name: 'John Doe',
            },
          },
        }).then(function(result) {
          // Handle the payment result (e.g., show a success message)
        });
      },
      error: function(xhr, status, error) {
        // Handle errors if any
      }
    });
  }
  