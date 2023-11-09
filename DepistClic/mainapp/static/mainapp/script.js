$(() => {
	// Stores the current page question order
	let currentQuestionOrder = parseInt($("#pass-btn").data('question-order'));

	// Pass the question without storing the value
	$("#pass-btn").click(() => {
		let nextQuestionOrder = currentQuestionOrder + 1;
		let url = '/questions/' + nextQuestionOrder;
		window.location.href = url;
	});

	// Go back to the previous question
	$("#back-btn").click(() => {
		let prevQuestionOrder = currentQuestionOrder - 1;
		if (prevQuestionOrder >= 1) {
			let url = '/questions/' + prevQuestionOrder;
			window.location.href = url;
		}
	});
	
	// Go home button with alert
	$("#home-btn").click(() => {
		const confirmation = window.confirm("Voulez-vous vraiment revenir, vous allez perdre les données en cours")
		if (confirmation) {
			window.location.href = "/";
		}
	});

	// Submit the form when one input is chosen
	$('input[type="radio"]').on('change', function() {
		$(this).closest('form').submit();
	});

	// Selects all elements with the info-icon class
	$('.info-icon').click(function(){
		// Get the ID of the modal to display
		var modalId = $(this).data('modal-toggle');
		// Selects modal by ID
		var modal = $('#' + modalId);
		// Display modal
		modal.removeClass('hidden');
		// Hide modal
		modal.find('.modal-close').click(function(){
			modal.addClass('hidden');
			// Keep scroll
			$('body').css('overflow', 'auto');
		});

		// Hide modal when the user click outside the content
		modal.click(function(event) {
			if (event.target === this) {
				//Hide modal
				modal.addClass('hidden');
				// Keep scroll
				$('body').css('overflow', 'auto');
			}
		});
	});

	// Add shadow when scrollPosition > 0
	$(window).scroll(function() {
		var scrollPosition = $(this).scrollTop();

		if (scrollPosition > 0) {
			$('header').addClass('shadow-lg transition duration-300');
		} else {
			$('header').removeClass('shadow-lg transition duration-300');
		}
	});

	// Hide form when submit
    $('#comment-form').on('submit', function(event) {
        event.preventDefault(); // Prevent form from submitting normally

        // Get comment
        const commentArea = $('#id_comment_area').val();

        // Send data
        $.ajax({
            type: 'POST',
            url: '/comment/',
            data: {
                comment_area: commentArea,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function(response) {
                // Display success message
                $('#comment-form').addClass('hidden');
                $('#success-message').removeClass('hidden');
            },
            error: function(error) {
                // Erro handeling
                console.error('Erreur lors de l\'envoi du commentaire :', error);
            }
        });
    });

	// Facebook Icon click
	$('#facebookIcon').on('click', function() {
		// Share on Facebook
		var url = 'https://www.facebook.com/sharer/sharer.php?u=' + encodeURIComponent('https://Depistclic.fr');
		window.open(url, '_blank');
	});

    // Twitter Icon click
    $('#twitterIcon').on('click', function() {
        // Share on Twitter
        var tweetUrl = 'https://twitter.com/intent/tweet?text=Votre%20message%20à%20partager&url=https:Depistclic.fr';
        window.open(tweetUrl, '_blank');
    });

    // LinkedIn Icon click
    $('#linkedinIcon').on('click', function() {
        // Share on LinkedIn
        var linkedinUrl = 'https://www.linkedin.com/sharing/share-offsite/?url=https://Depistclic.fr';
        window.open(linkedinUrl, '_blank');
    });
});
