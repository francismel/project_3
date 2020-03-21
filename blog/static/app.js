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

    $(element).hover(function () {
      $(element).popover('show');
    },
      function () {
        $(element).popover('hide');
        // hidePopover(element)
      });
  }



 function showComment(e) {
        console.log(e)
        $(e).append( $('.myDIV').attr("style","display: show") )

        // var x = document.getElementById("myDIV");
        // if (x.style.display === "none") {
        //   x.style.display = "block";
        // } else {
        //   x.style.display = "none";
        // }
      }


