from msclap import CLAP
import torch.nn.functional as F
import json
import argparse

# Define classes for zero-shot
# Should be in lower case and can be more than one word
classes = [
    'sneezing',
    'drinking sipping',
    'breathing',
    'brushing teeth',
    'water drops',
    'chirping of cicada',
    'typing',
    'street',
    'birds singing',
    'rustling leaves',
    'wind blowing',
    'thunderstorm',
    'ocean waves crashing',
    'flowing river',
    'sound of water flow',
    'rainfall',
    'crickets chirping',
    'frogs croaking',
    'wolves howling',
    'distant thunder',
    'owl hooting',
    'fire crackling',
    'bees buzzing',
    'waterfall',
    'cicadas buzzing',
    'distant forest sounds',
    'mountain stream',
    'animal footsteps in the forest',
    'morning bird chorus',
    'baby crying',
    'dog barking',
    'cat meowing',
    'doorbell ringing',
    'phone ringing',
    'clock ticking',
    'flush the toilet',
    'footsteps on gravel',
    'vacuum cleaner running',
    'blender',
    'microwave beeping',
    'washing machine',
    'shower running',
    'kettle boiling',
    'cutting vegetables',
    'frying food',
    'door opening',
    'pages flipping',
    'typing on a laptop',
    'printer printing',
    'applause',
    'people talking in a cafe',
    'crowd talking',
    'whispering',
    'traffic noise',
    'ambulance siren',
    'construction sounds',
    'crowd cheering',
    'lawnmower',
    'footsteps on wooden floor',
    'glass breaking',
    'train passing',
    'subway announcement',
    'keyboard typing',
    'printer working',
    'mouse clicking',
    'copier machine',
    'stapler',
    'phone conversation',
    'computer startup',
    'coffee machine',
    'water cooler',
    'paper shuffling',
    'elevator ding',
    'office chatter',
    'meeting room discussion',
    'footsteps in a hallway',
    'scanner beeping',
    'washing dishes',
    'television playing',
    'radio music',
    'child laughing',
    'door closing',
    'fridge humming',
    'eating sounds',
    'sipping coffee',
    'brushing hair',
    'window opening',
    'alarm clock ringing',
    'fan running',
    'fireplace burning',
    'blender blending',
    'vacuum cleaner',
    'car engine starting',
    'airplane flying overhead',
    'bus stopping',
    'bike bell ringing',
    'pedestrian crossing signal',
    'horns honking',
    'skateboard on pavement',
    'taxi driving by',
    'city square ambient noise',
    'construction drill',
    'street musician playing',
    'fountain in the park',
    'public announcement',
    'escalator in the mall',
    'footsteps in the subway',
    'church bells ringing',
    'amusement park rides',
    'ice cream truck music',
    'sports event cheering',
    'carnival sounds',
    'ship engine',
    'fireworks',
    'skate park',
    'playground laughter',
    'festival crowd noise',
    'motorcycle revving',
    'water poured into the cup,'
    'cock crowing',
    'string music',
    'piano music',
    'percussion music',
    'band performance',
    'symphony orchestra',
    'live concert',
    'modern cities',
]
ground_truth = ['motorcycle revving']
# Add prompt
prompt = 'this is a sound of '
class_prompts = [prompt + x for x in classes]

audio_files = []
parser = argparse.ArgumentParser(description="Sound recognition script.")
parser.add_argument("--audio_files", type=str, required=True, help="Path to the audio files.")
args = parser.parse_args()
audio_files = args.audio_files.split(',')

# Load and initialize CLAP
# Setting use_cuda = True will load the model on a GPU using CUDA
clap_model = CLAP(version = '2023', use_cuda=False)

# compute text embeddings from natural text
text_embeddings = clap_model.get_text_embeddings(class_prompts)

# compute the audio embeddings from an audio file
audio_embeddings = clap_model.get_audio_embeddings(audio_files, resample=True)

# compute the similarity between audio_embeddings and text_embeddings
similarity = clap_model.compute_similarity(audio_embeddings, text_embeddings)

similarity = F.softmax(similarity, dim=1)
values, indices = similarity[0].topk(5)

# print("Ground Truth: {}".format(ground_truth))
# print("Top predictions:\n")
# for value, index in zip(values, indices):
#     print(f"{classes[index]:>16s}: {100 * value.item():.2f}%")
max_value, max_index = max(zip(values, indices), key=lambda x: x[0].item())

# Output the class with the maximum value
predicted_class = classes[max_index]
json_output = json.dumps({"predicted_class": predicted_class})
print(json_output)