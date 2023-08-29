from mido import Message, MidiFile, MidiTrack
import numpy as np
from Sound.Sound import Sound
sound = Sound("SoundSample/5.wav")
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)
track.append(Message('program_change', program=0, time=0))

tblFreq = []
sample_size = 100
width = [1]
intensity = 11
for i in range(0, len(sound.monoSound)-1, sample_size):
    if i+sample_size < len(sound.monoSound)-1:
        chunk = sound.getChunk(i, i+sample_size)
    else:
        chunk = sound.getChunk(len(sound.monoSound)-(len(sound.monoSound)-i)-1, len(sound.monoSound)-1)
    xf = sound.getXf(chunk)
    yf = np.log10(np.abs(sound.getYf(chunk)))
    tblFreq.append(sound.getPeak(xf, yf, width, intensity))

tblNotes = []
for tblChunk in tblFreq:
    tbl = []
    for tblNote in tblChunk:
        if sound.find_nearest(sound.freqMIDI, tblNote[0]/2) not in tbl and sound.find_nearest(sound.freqMIDI, tblNote[0]/4) not in tbl and sound.find_nearest(sound.freqMIDI, tblNote[0]/8) not in tbl and sound.find_nearest(sound.freqMIDI, tblNote[0]/16) not in tbl and sound.find_nearest(sound.freqMIDI, tblNote[0]/32) not in tbl and sound.find_nearest(sound.freqMIDI, tblNote[0]/64) not in tbl and sound.find_nearest(sound.freqMIDI, tblNote[0]/128) not in tbl:
            tbl.append(np.where(sound.freqMIDI == tblNote)[0][0])
    tbl = np.unique(tbl)
    tblNotes.append(tbl)

time = 0
lastNote = tblNotes[0]
for tblNote in tblNotes:
    for note in np.setdiff1d(lastNote, tblNote):
        track.append(Message('note_off', channel=0, note=note, velocity=64, time=time))
    lastNote = tblNote
    for note in tblNote:
        #if note not in np.setdiff1d(tblNote, lastNote):
        track.append(Message('note_on', channel=0, note=note, velocity=64, time=time))
    time += 1
time += 10
for note in range(0, 127):
    track.append(Message('note_off', channel=0, note=note, velocity=64, time=time))

mid.save('new_song.midi')








#np.savetxt("SoundSample/dump", tblFreq, delimiter=',', newline='\n', encoding="utf8", fmt="%0.2f")#, fmt="%3.0f"
#Get the MIDI number from frequence
#print(np.where(sound.tblMIDI == sound.find_nearest(sound.freqMIDI, 440))[0][0])


#plt.plot(xf, yf)
#plt.show()


#chunk = sound.getChunk(0, 30)
#xf = sound.getXf(chunk)
#yf = np.log10(np.abs(sound.getYf(chunk)))
#tbl = sound.getPeak(xf, yf, [1, 2, 3], 10)
