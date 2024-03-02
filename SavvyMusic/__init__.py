#github https://github.com/Noob-savvy
#copyrighted 
from SavvyMusic.core.bot import Savvy
from SavvyMusic.core.dir import dirr
from SavvyMusic.core.git import git
from SavvyMusic.core.userbot import Userbot
from SavvyMusic.misc import dbb, heroku, sudo

from .logging import LOGGER

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

# Bot Client
app = Savvy()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
