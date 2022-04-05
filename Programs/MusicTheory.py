def getKey(key, mode):
    key = key.lower()
    mode = mode.lower()
    if (mode == "major"):
    	if (key == "c"):
        	return "The key of C has no sharps or flats."
    	elif (key == "f"):
        	return "The key of F has 1 flat: Bb."
    	elif (key == "bb" or key == "b flat"):
        	return "The key of Bb has 2 flats: Bb and Eb."
    	elif (key == "eb" or key == "e flat"):
        	return "The key of Eb has 3 flats: Bb, Eb, and Ab."
    	elif (key == "ab" or key == "a flat"):
        	return "The key of Ab has 4 flats: Bb, Eb, Ab, and Db."
    	elif (key == "db" or key == "d flat"):
        	return "The key of Db has 5 flats: Bb, Eb, Ab, Db, and Gb."
    	elif (key == "gb" or key == "g flat"):
        	return "The key of Gb has 6 flats: Bb, Eb, Ab, Db, Gb, and Cb."
    	elif (key == "cb" or key == "c flat"):
        	return "The key of Cb has 7 flats: Bb, Eb, Ab, Db, Gb, Cb, and Fb."
    	elif (key == "g"):
        	return "The key of G has 1 sharp: F#."
    	elif (key == "d"):
        	return "The key of D has 2 sharps: F# and C#."
    	elif (key == "a"):
        	return "The key of A has 3 sharps: F#, C#, and G#."
    	elif (key == "e"):
        	return "The key of E has 4 sharps: F#, C#, G#, and D#."
    	elif (key == "b"):
        	return "The key of B has 5 sharps: F#, C#, G#, D#, and A#."
    	elif (key == "f#" or key == "f sharp"):
        	return "The key of F# has 6 sharps: F#, C#, G#, D#, A#, and E#."
    	elif (key == "c#" or key == "c sharp"):
        	return "The key of C# has 7 sharps: F#, C#, G#, D#, A#, E#, and B#
    elif (mode == "minor"):
        if (key == "a" or key == "a minor"):
        	return "The key of A minor has no sharps or flats."
    	elif (key == "d" or key == "d minor"):
        	return "The key of D minor has 1 flat: Bb."
    	elif (key == "g" or key == "g minor"):
        	return "The key of G minor has 2 flats: Bb and Eb."
    	elif (key == "c" or key == "c minor"):
        	return "The key of C minor has 3 flats: Bb, Eb, and Ab."
    	elif (key == "f" or key == "f minor"):
        	return "The key of F minor has 4 flats: Bb, Eb, Ab, and Db."
    	elif (key == "bb" or key == "bb minor" or key == "b flat" or key == "b flat minor"):
        	return "The key of Bb minor has 5 flats: Bb, Eb, Ab, Db, and Gb."
    	elif (key == "eb" or key == "eb minor" or key == "e flat" or key == "e flat minor"):
        	return "The key of Eb minor has 6 flats: Bb, Eb, Ab, Db, Gb, and Cb."
    	elif (key == "ab" or key == "ab minor" or key == "a flat" or key == "a flat minor"):
        	return "The key of Ab minor has 7 flats: Bb, Eb, Ab, Db, Gb, Cb, and Fb."
    	elif (key == "e" or key == "e minor"):
        	return "The key of E minor has 1 sharp: F#."
    	elif (key == "b" or key == "b minor"):
        	return "The key of B minor has 2 sharps: F# and C#."
    	elif (key == "f#" or key == "f# minor" or key == "f sharp" or key == "f sharp minor"):
        	return "The key of F# minor has 3 sharps: F#, C#, and G#."
    	elif (key == "c#" or key == "c# minor" or key == "c sharp" or key == "c sharp minor"):
        	return "The key of C# minor has 4 sharps: F#, C#, G#, and D#."
    	elif (key == "g#" or key == "g# minor" or key == "g sharp" or key == "g sharp minor"):
        	return "The key of G# minor has 5 sharps: F#, C#, G#, D#, and A#."
    	elif (key == "d#" or key == "d# minor" or key == "d sharp" or key == "d sharp minor"):
        	return "The key of D# minor has 6 sharps: F#, C#, G#, D#, A#, and E#."
    	elif (key == "a#" or key == "a# minor" or key == "a sharp" or key == "a sharp minor"):
        	return "The key of A# minor has 7 sharps: F#, C#, G#, D#, A#, E#, and B#
    
def findKey (sharps, flats, mode):
    mode = mode.lower()
    if (mode == "major"):
    	if (sharps == 0 and flats == 0):
        	return "The key with 0 flats and 0 sharps is C."
    	elif (sharps == 0):
        	if (flats == 1):
            	return "The key with 1 flat is F."
        	elif (flats == 2):
            	return "The key with 2 flats is Bb."
        	elif (flats == 3):
            	return "The key with 3 flats is Eb."
        	elif (flats == 4):
            	return "The key with 4 flats is Ab."
        	elif (flats == 5):
            	return "The key with 5 flats is Db."
        	elif (flats == 6):
            	return "The key with 6 flats is Gb."
        	elif (flats == 7):
            	return "The key with 7 flats is Cb."
    	elif (flats == 0):
        	if (sharps == 1):
            	return "The key with 1 sharp is G."
        	elif (sharps == 2):
            	return "The key with 2 sharps is D."
        	elif (sharps == 3):
            	return "The key with 3 sharps is A."
        	elif (sharps == 4):
            	return "The key with 4 sharps is E."
        	elif (sharps == 5):
            	return "The key with 5 sharps is B."
        	elif (sharps == 6):
            	return "The key with 6 sharps is F#."
        	elif (sharps == 7):
            	return "The key with 7 sharps is C#."
    elif (mode == "minor"):
        if (sharps == 0 and flats == 0):
            return "The key with 0 flats and 0 sharps is A minor"
        elif (sharps == 0):
        	if (flats == 1):
            	return "The key with 1 flat is D minor."
        	elif (flats == 2):
            	return "The key with 2 flats is G minor."
        	elif (flats == 3):
            	return "The key with 3 flats is C minor."
        	elif (flats == 4):
            	return "The key with 4 flats is F minor."
        	elif (flats == 5):
            	return "The key with 5 flats is Bb minor."
        	elif (flats == 6):
            	return "The key with 6 flats is Eb minor."
        	elif (flats == 7):
            	return "The key with 7 flats is Ab minor."
    	elif (flats == 0):
        	if (sharps == 1):
            	return "The key with 1 sharp is E minor."
        	elif (sharps == 2):
            	return "The key with 2 sharps is B minor."
        	elif (sharps == 3):
            	return "The key with 3 sharps is F# minor."
        	elif (sharps == 4):
            	return "The key with 4 sharps is C# minor."
        	elif (sharps == 5):
            	return "The key with 5 sharps is G# minor."
        	elif (sharps == 6):
            	return "The key with 6 sharps is D# minor."
        	elif (sharps == 7):
            	return "The key with 7 sharps is A# minor."
            
        
