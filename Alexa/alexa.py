#pip install pywhatkit->powerful pkg to search utube
import speech_recognition as sr  #so that alexa recognizes our speech
import pyttsx3 #ppttsx python text to speech
import pywhatkit
import datetime
import wikipedia			#pip install wikipedia to get info from wikipedia
import pyjokes			#pip install pyjokes->if we are bored and we want jokes
import requests, json , sys  #remaining to be installed

listener=sr.Recognizer()
engine=pyttsx3.init()
#to get female voice of alexa declaring varialble voices
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
	engine.say(text)
	engine.runAndWait()

def weather(city):
    # Enter your API key here 
    api_key = "<YOUR API KEY"
    
    # base_url variable to store url 
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # Give city name 
    city_name = city
    
    # complete_url variable to store 
    # complete url address 
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
    
    # get method of requests module 
    # return response object 
    response = requests.get(complete_url) 
    
    # json method of response object  
    # convert json format data into 
    # python format data 
    x = response.json() 
    
    # Now x contains list of nested dictionaries 
    # Check the value of "cod" key is equal to 
    # "404", means city is found otherwise, 
    # city is not found 
    if x["cod"] != "404": 
    
        # store the value of "main" 
        # key in variable y 
        y = x["main"] 
    
        # store the value corresponding 
        # to the "temp" key of y 
        current_temperature = y["temp"] 
    
        # store the value corresponding 
        # to the "pressure" key of y 
        #current_pressure = y["pressure"] 
    
        # store the value corresponding 
        # to the "humidity" key of y 
        #current_humidiy = y["humidity"] 
    
        # store the value of "weather" 
        # key in variable z 
        #z = x["weather"] 
    
        # store the value corresponding  
        # to the "description" key at  
        # the 0th index of z 
        #weather_description = z[0]["description"]
        return str(current_temperature)
    
        # print following values 
        '''print(" Temperature (in kelvin unit) = " +
                        str(current_temperature) + 
            "\n atmospheric pressure (in hPa unit) = " +
                        str(current_pressure) +
            "\n humidity (in percentage) = " +
                        str(current_humidiy) +
            "\n description = " +
                        str(weather_description)) 
    else: 
        print(" City Not Found ")
        '''


def take_command():
	try:
		with sr.Microphone() as source:
			print("listening...")
			voice=listener.listen(source)
			command=listener.recognize_google(voice)
			command=command.lower()
			if 'alexa' in command:
				command=command.replace('alexa','')
				print(command)
	except:
		pass
	return command

def run_alexa():
	command=take_command()
	print(command)
	if 'play' in command:
		song=command.replace('play','')
		talk('playing'+song)
		pywhatkit.playonyt(song)
	elif 'time' in command:
		#time=datetime.datetime.now().strftime('%H:%M')
		#to get am and pm time
		time=datetime.datetime.now().strftime('%I:%M %p')
		print(time)
		talk('Current time is '+time)
	elif 'who the heck is' in command:
		person=command.replace('who the heck is','')
		info=wikipedia.summary(person,1)
		print(info)
		talk(info)
	elif 'who is' in command:
		person=command.replace('who is','')
		info=wikipedia.summary(person,1)
		print(info)
		talk(info)
	elif 'How' in command:
		person=command.replace('How','')
		info=wikipedia.summary(person,1)
		print(info)
		talk(info)
	elif 'what' in command:
		person=command.replace('what','')
		info=wikipedia.summary(person,1)
		print(info)
		talk(info)
	elif 'which' in command:
		person=command.replace('which','')
		info=wikipedia.summary(person,1)
		print(info)
		talk(info)
	elif 'where' in command:
		person=command.replace('where','')
		info=wikipedia.summary(person,1)
		print(info)
		talk(info)
	elif 'joke' in command:
		talk(pyjokes.get_joke())
	elif 'weather' in command:
        	talk('Please tell the name of the city')
        	city = take_command()
        	#weather_api = weather('Hong Kong')
        	weather_api = weather(city)
        	talk(weather_api + 'degree fahreneit' )
	elif 'stop' in command:
       	 sys.exit()
	
	else:
		talk('Please say the command again')

#strftime->string of time
while True:
	run_alexa()