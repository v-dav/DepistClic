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

	// 
	$('.info-icon').click(function () {
		let testId = $(this).data('test-id');
		var infoElement = $('.test-info[data-test-id="' + testId + '"]');
		infoElement.toggleClass("hide");
	});

	// Add shadow when scroll
	$(window).scroll(function() {
		var scrollPosition = $(this).scrollTop();

		if (scrollPosition > 0) {
			$('header').addClass('shadow-lg transition duration-300');
		} else {
			$('header').removeClass('shadow-lg transition duration-300');
		}
	});
});
