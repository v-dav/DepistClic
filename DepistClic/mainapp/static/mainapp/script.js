$(() => {
	let currentQuestionOrder = parseInt($("#pass-btn").data('question-order'));

	$("#pass-btn").click(() => {
		let nextQuestionOrder = currentQuestionOrder + 1;
		let url = '/questions/' + nextQuestionOrder;
		window.location.href = url;
	});

	$("#back-btn").click(() => {
		let prevQuestionOrder = currentQuestionOrder - 1;
		if (prevQuestionOrder >= 1) {
			let url = '/questions/' + prevQuestionOrder;
			window.location.href = url;
		}

	});

	// Form handling
	$("#question-form").submit((event) => {
		event.preventDefault(); // Empêche l'envoi par défaut du formulaire

		// Récupère la valeur de l'utilisateur depuis le champ de texte et supprime les espaces inutiles
		let userAnswer = $("#user-answer").val().trim();

		// Vérifie si l'utilisateur a saisi une valeur
		if (userAnswer !== '') {

			// Récupère le jeton CSRF depuis le formulaire
			let csrfToken = $('[name=csrfmiddlewaretoken]').val();

			// Envoie la valeur au serveur via une requête AJAX
			$.ajax({
				url: '/store_value/', // URL de la vue Django pour enregistrer la valeur
				type: 'POST', // Méthode POST pour envoyer des données au serveur
				data: { user_answer: userAnswer, question_order: currentQuestionOrder }, // Données à envoyer au serveur
				headers: {
					'X-CSRFToken': csrfToken // Utilise le jeton CSRF récupéré pour authentifier la requête
				},
				success: function (response) {
					let nextQuestionOrder = currentQuestionOrder + 1;
					let url = '/questions/' + nextQuestionOrder;
					window.location.href = url; // Redirige l'utilisateur vers la prochaine question
				},
				error: function (error) {
					// Gère les erreurs en cas d'échec de la requête
					console.log(error);
				}
			});
		} else {
			// Affiche un message d'erreur si l'utilisateur n'a pas saisi de valeur
			alert("Entrez une valeur valide");
		}
	});

});
