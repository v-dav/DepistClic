$(() => {
	let currentQuestionId = parseInt($("#pass-btn").data('question-id'));

	$("#pass-btn").click(() => {
		let nextQuestionId = currentQuestionId + 1;
		let url = '/questions/' + nextQuestionId;
		window.location.href = url;
	});

	$("#back-btn").click(() => {
		let prevQuestionId = currentQuestionId - 1;
		let url = '/questions/' + prevQuestionId;
		window.location.href = url;
	});

});
