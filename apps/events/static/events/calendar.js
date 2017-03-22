/* global eventsData */
const Flatpickr = require('flatpickr')
const FlatpickrLocale = require('flatpickr/dist/l10n/de.js')
const $ = require('jquery')

const calendar = document.getElementById('calendar')

if (calendar) {
  const $events = $('.calendar-list__item')
  const selectorPattern = '[data-date^="{}"]'

  let calendarFlatpickr = new Flatpickr(calendar, {
    inline: true,
    locale: FlatpickrLocale[$('html').attr('lang')],
    enable: [
      date => {
        return eventsData.some(eventObj => {
          let dateParts = eventObj.date.split('-')
          let year = parseInt(dateParts[0], 10)
          let month = parseInt(dateParts[1], 10)
          let day = parseInt(dateParts[2], 10)
          return date.getFullYear() === year
            && date.getMonth() + 1 === month
            && date.getDate() === day
        })
      }
    ],
    onMonthChange: (selectedDates, dateStr, instance) => {
      let selectorString = getSelectorString(instance)
      updateList(selectorString)
    },
    onYearChange: (selectedDates, dateStr, instance) => {
      let selectorString = getSelectorString(instance)
      updateList(selectorString)
    },
    onReady: (selectedDates, dateStr, instance) => {
      let selectorString = getSelectorString(instance)
      updateList(selectorString)
    },
    onChange: (selectedDates, dateStr, instance) => {
      let selectorString = getSelectorString(instance, dateStr.slice(-2))
      highlightDate(selectorString)
    }
  })

  function getSelectorString (instance, day = '') {
    let date = instance.currentYear + '-' + (instance.currentMonth + 1)
    if (day) {
      date += '-' + day
    }
    return selectorPattern.replace('{}', date)
  }

  function updateList (selector) {
    let $currentMonthEvents = $events.filter(selector)

    $events.removeClass('is-active')
    $currentMonthEvents.addClass('is-active')
  }

  function highlightDate (selector) {
    let $event = $(selector)

    $events.filter('.is-highlighted').removeClass('is-highlighted')
    $event.addClass('is-highlighted')
  }
}
