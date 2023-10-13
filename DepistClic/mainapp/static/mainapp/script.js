$(() => {
    let currentQuestionId = parseInt($("#pass-btn").data('question-id'));

    $("#pass-btn").click(() => {
        let nextQuestionId = currentQuestionId + 1;
        let url = '/questions/' + nextQuestionId;
        window.location.href = url;
    });

    $("#back-btn").click(() => {
        let prevQuestionId = currentQuestionId - 1;
		if (prevQuestionId >= 1) {
			let url = '/questions/' + prevQuestionId;
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
				data: { user_answer: userAnswer }, // Données à envoyer au serveur
				headers: {
					'X-CSRFToken': csrfToken // Utilise le jeton CSRF récupéré pour authentifier la requête
				},
				success: function(response) {
					let nextQuestionId = currentQuestionId + 1;
					let url = '/questions/' + nextQuestionId;
					window.location.href = url; // Redirige l'utilisateur vers la prochaine question
				},
				error: function(error) {
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