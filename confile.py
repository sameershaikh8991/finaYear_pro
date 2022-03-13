import os
import configparser

class Setup:
    def start_sconfig(self, config):
        userdata = 'user'
        config.add_section('user')

        bot_name = str(input("Enter Assistant name (default=jarvis): ") or "jarvis")
        user_name = str(input("Enter User name (default=sir): ") or "sir")
        # user_name = str(input("choose voice (male:0 or Female:1) (default=Male): ") or "0")
        # bot_name = str(input("Enter Bot name (default=jarvis): ") or "jarvis")
        # photos_dir = str(input("Enter Photos Directories separated by comma ',' (default=None): ") or "None")
        song_dir = str(input("Enter song Directories separated by comma ',' (default=None): ") or "None")

        config[userdata]['bot_name'] = bot_name
        config[userdata]['user_name'] = user_name
        # config[userdata]['photos'] = photos_dir
        config[userdata]['song'] = song_dir
        # config[userdata]['voice'] = voiceMF

        with open('C:/Users/'+os.getlogin()+'/jarvis/config.ini', 'w') as configfile:
            config.write(configfile)

        print("Setup Done")
        return True

    def setup_assistant(self):
        if not os.path.exists('C:/Users/'+os.getlogin()+'/jarvis'):
            os.makedirs('C:/Users/'+os.getlogin()+'/jarvis')
        config = configparser.ConfigParser()

        if os.path.exists('C:/Users/'+os.getlogin()+'/jarvis'):
            sure = str(input("setup your Ai (y or n):") or "n")
            if sure == "n":
                print("No changes done")
                return False
            else:
                return self.start_sconfig(config)
        else:
            return self.start_sconfig(config)
