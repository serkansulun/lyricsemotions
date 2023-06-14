Emotion classification of MIDI lyrics

To only download the datasets, with pairs of MIDI file names and predicted emotions from the lyrics, you can right-click and choose "Save Link As...", using the links below:

[7-labels](https://raw.githubusercontent.com/emotionalmusic/lyricsemotions/master/datasets/7labels.csv)

[28-labels](https://raw.githubusercontent.com/emotionalmusic/lyricsemotions/master/datasets/28labels.csv)

Required Python packages: transformers, pretty_midi

Usage:

`python main.py --midi_file_path "John Lennon - Imagine.mid"`

or

`python main.py --lyrics "I hope some day you'll join us. And the world will be as one"`