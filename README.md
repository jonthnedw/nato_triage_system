Digital Triage Assistant.

===Discussion===
I think we should use a centralized info model where we store the parameters in some sort of db (maybe a data structure or our own custom class) and then systems can make requests to the model for the info that they need. A more detailed example of how this would work:

  1. We have 23/33 systems requesting heart rate so that's the first parameter we ask for.
    1a. During this entire process, systems are constantly probing the db for the info that they need so they can be updated in realtime.
  2. Heart rate is supplied and is fed to the systems. No system has enough info yet so nothing conclusive is shown to the user. 17/33 systems need blood pressure so that's the next parameter we ask for.
  3. We continue asking for parameters and systems continue to probe the central db for the info they need until they can reach a conclusion.
  4. The outputs of the systems all go back to some central source that we can use to do VSM and render the results to the GUI.
    4a. The user can stop inputting info when they/we(?) feel there's enough info to make an informed decision. (Maybe it's a list of like 30 parameters, but we can show a 95% confidence at 11 parameters filled or something)
    
Now in terms of actually programming it, I think that we need to have a separate .py for the central db, and it might do us well to just make it a custom class. The underlying data structure for parameter data could just simply be a hashmap or something, but having the wrapping custom class lets us interface with the data structure with a lot more finesse. I'm imagining the central db would have some sort of request method that takes in a label and returns the matching data to the requesting model. So:

def get_data(string label):
  #find label in hashmap
  return label
  
Thus, each system just needs to call db.get_data(label), maybe asynchronously, and use it in its own calculations. The only other thing I think we would need that I haven't mentioned is an agreed upon dictionary of labels. So "heart_rate" as opposed to "heartRate" or however we want to do that. If we were to follow PEP 8, we should use "all_lowercase_letters_with_words_separated_by_underscores".

As far as the abstract for the systems, I think that's up to your judgement about what should be inherited. Since the database will have a method to hand out data, there's no need for each system to have a method to request data. However, you may want to think about if there's a clever way to abstract storing the data in each system. So instead of:

  heart_rate = db.get_data(heart_rate)
  blood_pressure = db.get_data(blood_pressure)
  
Maybe there's some other way of abstracting that? If we use the agreed labels, I know python can call passed variables like:

  for x in list:
    info.append(db.get_data(x))
    
  where list is the list of parameters the system needs with proper label names (also, idk if append is good pythonic code, I highly doubt it is)

Message me if you have any questions.

-David
