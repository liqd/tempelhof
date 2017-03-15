var $ = require('jquery')

$(function () {
  $('[data-toggle="collapse"]').each(function (index, toggle) {
    let $toggle = $(toggle);
    let $target = $($toggle.attr('href'))

    $toggle.click(function (event) {
      event.preventDefault()
      if ($toggle.is('[aria-expanded="true"]')) {
        $target.slideUp()
        $toggle.attr('aria-expanded', 'false');
      } else {
        $target.slideDown()
        $toggle.attr('aria-expanded', 'true');
      }
    })

    if (!$toggle.is('[aria-expanded="true"]')) {
      $target.hide()
    }
  })
})
