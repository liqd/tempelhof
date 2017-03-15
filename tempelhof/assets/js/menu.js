var $ = require('jquery')

const $headerToggle = $('.header__toggle')
const $headerList = $('.header__list')

$headerToggle.on('click', function() {
  $headerList.toggleClass('is-active')
  $headerToggle.find('i').toggleClass('fa-times fa-bars')
})
