$(() => {
	let nextQuestionId = parseInt($("#pass-btn").data('question-id')) + 1
	$("#pass-btn").click(() => {
		$.get('/questions/' + nextQuestionId, (data) => {
			$("#question_title").html(data.title)
		})
		nextQuestionId += 1;
	})
});
