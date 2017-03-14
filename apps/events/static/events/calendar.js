const Flatpickr = require('flatpickr')

const calendar = document.getElementById('calendar')

var a = new Flatpickr(calendar, {
  inline: true,
  enable: [
    date => {
      return eventsData.filter(eventObj => {
        // django outputs the date in iso-format which JS parses as local time
        // possibly adding one or two hours
        let eventDate = new Date(eventObj.date).setHours(0)
        return date.getTime() === eventDate
      }).length
    }
  ]
})
