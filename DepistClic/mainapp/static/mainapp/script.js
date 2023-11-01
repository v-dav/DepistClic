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

    // Toggle the visibility of the info card
    $(document).on('click', '.info-icon', function(event) {
        event.stopPropagation();
        var testId = $(this).data('test-id');
        var infoCard = $('.info-card[data-test-id="' + testId + '"]');
        infoCard.toggleClass('hidden');
    });

    // Hide the visibility of the info card
    $(document).click(function(event) {
        // If the click event occurred outside any info card
        if (!$(event.target).closest('.info-card').length && !$(event.target).is('.info-icon')) {
            $('.info-card').addClass('hidden');
        }
    });

    // Stores the state of the menu
    let isMenuOpen = false;

    // Toggle the visibility of the menu on menu button click
    $("#menu-toggle").click(() => {
        if (isMenuOpen) {
            $("#menu").addClass("hidden");
        } else {
            $("#menu").removeClass("hidden");
        }
        isMenuOpen = !isMenuOpen;
    });

    // Handle clicks on menu items
    $("#menu").click(() => {
        // Close the menu when a menu item is clicked
        $("#menu").addClass("hidden");
        isMenuOpen = false;
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
});