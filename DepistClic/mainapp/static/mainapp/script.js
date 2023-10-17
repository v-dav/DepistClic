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

	// Form handling
	$("#question-form").submit((event) => {
		// Prevents sending the form by default
		event.preventDefault();

		// Get the value inupt and trim unneeded white spaces
		let userAnswer = $("#user-answer").val().trim();

		// Check if the user have written a value
		if (userAnswer !== '') {

			// Get the CSRF token from the form
			let csrfToken = $('[name=csrfmiddlewaretoken]').val();

			// Send AJAX request with the value and current question order
			$.ajax({
				url: `/questions/${currentQuestionOrder}/`,
				type: 'POST',
				data: { user_answer: userAnswer, question_order: currentQuestionOrder },
				headers: {
					'X-CSRFToken': csrfToken // Used to authenticate the request
				},
				// Redirects the user to the next question
				success: function (response) {
					let nextQuestionOrder = currentQuestionOrder + 1;
					let url = '/questions/' + nextQuestionOrder;
					window.location.href = url;
				},
				error: function (error) {
					console.log(error);
				}
			});
		} else {
			// Affiche un message d'erreur si l'utilisateur n'a pas saisi de valeur
			alert("Entrez une valeur valide");
		}
	});

});
