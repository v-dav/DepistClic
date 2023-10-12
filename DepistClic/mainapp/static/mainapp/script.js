$(() => {
	let nextQuestionId = parseInt($("#pass-btn").data('question-id')) + 1
	$("#pass-btn").click(() => {
		window.location.href = '/questions/' + nextQuestionId;
		nextQuestionId += 1;
	})
});
