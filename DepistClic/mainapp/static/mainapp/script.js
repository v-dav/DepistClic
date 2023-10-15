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

	$('input[type="submit"]').click((event) => {
		event.preventDefault();
		const answerText = $('textarea[name="answer_text"]').val();
		if (answerText === "") {
			alert("Saisissez une valeur");
		} else {
			let nextQuestionOrder = currentQuestionOrder + 1;
			let url = '/questions/' + nextQuestionOrder;
			window.location.href = url;
		}
	})
});
