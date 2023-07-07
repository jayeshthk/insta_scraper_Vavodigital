const axios = require('axios');
const cron = require('node-cron');

//make sure fastapi running 
const url = 'http://0.0.0.0:8000/insta_collector';
const headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json'
};

//input json , editable just change username as per desired username and is_save to false in order to avoid saving posts.
const data = {
  username: 'future',
  is_save: true
};

// Schedule the task to run every 24 hours
cron.schedule('0 0 * * *', () => {
  axios.post(url, data, { headers })
    .then(response => {
      console.log('Response:', response);
    })
    .catch(error => {
      console.error('Error:', error);
    });
});
