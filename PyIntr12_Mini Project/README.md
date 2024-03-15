# Mini Project: 
## Design software for video media management.
- Implement store practice facilities, such as menu design, adding, editing, deleting, searching, etc.
- Design a general class called Media that includes the following features.
   - properties: 
name - director - IMDB score - url - duration - casts
   - methods: showInfo - download -
- Then create the following classes that inherit from the Media class.
  - Film
  - Series
  - Documentary
  - Clip (short film)
- Define different features for the above classes as you wish. For example, a series can have a property called (number of episodes), while a movie does not have this property.
- Define a class named Actor for actors. The casts attribute in the Media class is a list of Actors.
- At the beginning of the program, information should be read from the file and when exiting the program, new changes will be saved in the file.
- Implement each class in a separate file that must be imported in main.py.
- Design an advanced search function that receives two times a and b in minutes from the user and displays videos whose duration is between a and b.
- If the user calls the download method for a video, download it using pytube according to the url. (Refer to @pylearn Instagram address for guidance)