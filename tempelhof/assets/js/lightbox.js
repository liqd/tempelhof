const $ = require('jquery')
const $colorbox = require('jquery-colorbox')

$('.lightbox-group').colorbox({
  rel: 'lightbox-group',
  transition: 'fade',
  className: 'colorbox',
  maxWidth: '80%',
  maxHeight: '80%',
  close: '<i class="fa fa-close" aria-label="Galerie schließen"></i>',
  previous: '<i class="fa fa-chevron-left" aria-label="vorheriges Foto"></i>',
  next: '<i class="fa fa-chevron-right" aria-label="nächstes Foto"></i>',
  current: 'Bild {current} von {total}'
});
