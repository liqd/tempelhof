const Flatpickr = require('flatpickr')

const calendar = document.getElementById('calendar')

var a = new Flatpickr(calendar, {
  inline: true,
  enable: [
    date => {
      return eventsData.some(eventObj => {
        let dateParts = eventObj.date.split('-')
        let year = parseInt(dateParts[0], 10)
        let month = parseInt(dateParts[1], 10)
        let day = parseInt(dateParts[2], 10)
        let eventDate = new Date(year, month, day)
        return date.getFullYear() === year
          && date.getMonth() === month
          && date.getDate() === day
      })
    }
  ]
})
