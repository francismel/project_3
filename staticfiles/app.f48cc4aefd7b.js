function showProfile(element) {

    $(element).popover({
      container: 'body',
      html: true,
      viewport: { selector: "body", padding: 0 },
      content: function () {
        return $('#profile-wrapper').html();
      }
    });
    $(element).popover('show');

    // $(element).hover(function () {
    // //   $(element).popover('show');
    // // // },
    //   function () {
    //     $(element).popover('hide');
    //     // hidePopover(element)
    //   });
  }


