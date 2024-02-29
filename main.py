import transformers
import pretty_midi
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--n_labels", type=int, choices=(7, 28), default=28,
    help="Number of labels to output, 7 or 28.")
parser.add_argument("--midi_file_path", type=str,
    help="Path to the MIDI file")
parser.add_argument("--lyrics", type=str,
    help="Song lyrics, must be in quotes")
args = parser.parse_args()

assert args.midi_file_path != None or args.lyrics != None, \
    "Either MIDI file path or lyrics must be provided."

assert not (args.midi_file_path != None and args.lyrics != None), \
    "Cannot provide BOTH MIDI file path and lyrics."

model_dir = f'models/labels{args.n_labels}'
tokenizer = transformers.AutoTokenizer.from_pretrained(model_dir)
model = transformers.AutoModelForSequenceClassification.from_pretrained(model_dir)
pipeline = transformers.pipeline("text-classification", model=model, tokenizer=tokenizer, top_k=None)
    
if args.midi_file_path != None:
    mid = pretty_midi.PrettyMIDI(args.midi_file_path)
    lyrics = "".join([lyric.text for lyric in mid.lyrics])
else:
    lyrics = args.lyrics

emotions = pipeline(lyrics, truncation=True)[0]

[print(f'{emotion["label"]:15s}: {emotion["score"]:.4f}') for emotion in emotions]
lyrics = lyrics.replace("\r", "\n")
print("\nLyrics:")
print(lyrics)

