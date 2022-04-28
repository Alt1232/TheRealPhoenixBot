from tg_bot.sample_config import Config


class Development(Config):
    OWNER_ID =  1174557449 # my telegram ID
    OWNER_USERNAME = "rqveriie"  # my telegram username
    API_KEY = "5393515983:AAEC2btjfmPriBwKL387qGGnR8Wa6pQ_Hjc"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost:5432/database'  # sample db credentials
    MESSAGE_DUMP = '-1001734388320' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [1174557449]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']

