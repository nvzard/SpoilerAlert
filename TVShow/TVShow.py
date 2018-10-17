import requests

from bs4 import BeautifulSoup


NO_INFORMATION = 'Sorry, no info about the next episode of {} is available yet.'
SHOW_FINISHED = 'The show has finished streaming all its episodes. (No further information available)'
WRONG_SHOW_NAME = '**ERROR** The TV Show name you entered is not correct.'
DATES_FOUND = 'Brace yourself, the next epsiode(i.e. {}) will release on {}. CountDown: {}.'


class TVShow():

    def __init__(self, name):
        self.name = name
        self.status = self.get_status()

    @staticmethod
    def get_show_url(show_name):
        """
        Get URL of the TV Show's webpage

        :param show_name: Name of TV Show

        :return: URL of the TV Show's webpage
        """
        show_name = show_name.replace(' ', '-')
        URL = 'https://next-episode.net/' + show_name
        return URL

    @staticmethod
    def findValue(key, text):
        """
        Filter scraped data and find the useful keys

        :param key: String to search for in text
        :param text: String that will be searched

        :return: Filtered result as per the key
        """
        key_start_index = text.find(key)
        trim_start = text[key_start_index:]
        trim_end = trim_start[:trim_start.find('\n')]

        return trim_end.strip()

    @staticmethod
    def filter_legit_data(text):
        """
        Filter useful data from the scraped data

        :param text: Raw data that needs to be filtered

        :return: Dictionary of useful data for next episode's status
        """
        date = TVShow.findValue('Date', text)
        name = TVShow.findValue('Name', text)
        time_left = TVShow.findValue('Countdown', text)

        status_dict = {
            'episode_name': name[5:],
            'date': date[5:],
            'countdown': time_left[10:],
        }

        return status_dict

    @staticmethod
    def filter_extra_information(text):
        """
        Filter useful data from the scraped data

        :param text: Raw data that needs to be filtered

        :return: Dictionary of useful data for next episode's status
        """
        prediction = text[text.find('.')+1:].strip()

        status_dict = {
            'extra_info': prediction,
        }

        return status_dict

    @staticmethod
    def scrape_next_episode_status(show_url, show_name):
        """
        Main web-scraping logic to get status of the next episode

        :param show_url: URL of TV Show's webpage
        :param show_name: Name of the TV Show

        :return: Status of the next episode
        """
        page = requests.get(show_url)
        if page.status_code == 404:
            return WRONG_SHOW_NAME

        soup = BeautifulSoup(page.text, 'html.parser')
        next_episode = soup.find('div', attrs={'id':'next_episode'})
    
        if next_episode is None:
            return SHOW_FINISHED

        if next_episode.text.find('Countdown') == -1:
            status_dict = TVShow.filter_extra_information(next_episode.text)
            status = NO_INFORMATION.format(show_name.title())
            if len(status_dict['extra_info']):
                status += '\n\nBonus information:\n'
                status += status_dict['extra_info']
        else:
            status_dict = TVShow.filter_legit_data(next_episode.text)
            status = DATES_FOUND.format(
                        status_dict['episode_name'],
                        status_dict['date'],
                        status_dict['countdown'],
                    )
        return status
    
    def get_status(self):
        """
        Get status of the next episode of TV Show

        :return: Status of the TV Show's next episode
        """
        show_url = self.get_show_url(self.name)
        next_episode_status = self.scrape_next_episode_status(show_url, self.name)

        # Format the status of the next episode
        response = 'Show Name: '
        response += self.name.title() + '\n'
        response += 'Status:\n'
        response += next_episode_status
        response += '\n\n'

        return response
