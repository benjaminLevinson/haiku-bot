import os

import twitter
import random


def tweet(text):
    api = twitter.Api(consumer_key=os.getenv("HAIKU_CONSUMER_KEY"),
                      consumer_secret=os.getenv("HAIKU_CONSUMER_SECRET"),
                      access_token_key=os.getenv("HAIKU_ACCESS_TOKEN_KEY"),
                      access_token_secret=os.getenv("HAIKU_ACCESS_TOKEN_SECRET"))
    api.PostUpdate(text)


def random_syllables(num):
    line = []
    while sum(line) < num:
        random_num = random.randrange(1, 5)

        if sum(line)+random_num > num:
            continue

        line.append(random_num)
    return line


def get_line_layout(line):
    line = list(map(str, line))
    adv = 'syllableadverbs'
    adj = 'syllableadjectives'
    noun = 'syllablenouns'
    verb = 'syllableverbs'
    part_of_speech_line = []
    len7 = [adv, adv, adj, adj, noun, verb, noun]
    len6 = [adv, adv, adj, noun, verb, noun]
    len5 = [adv, adj, noun, verb, noun]
    len4 = [adj, noun, verb, noun]
    len3 = [noun, verb, noun]
    len2 = [noun, verb]
    len1 = [noun]
    line_lens = [len1, len2, len3, len4, len5, len6, len7]
    for index, part_speech in enumerate(line_lens[len(line)-1]):
        part_of_speech_line.append(line[index]+part_speech)
    return part_of_speech_line


def generate_haiku():
    line1 = random_syllables(5)
    line2 = random_syllables(7)
    line3 = random_syllables(5)

    haiku_layout = [line1, line2, line3]
    haiku_part_of_speech = []

    for line in haiku_layout:
        haiku_part_of_speech.append(get_line_layout(line))

    haiku = []
    for line in haiku_part_of_speech:
        haiku_line = []
        for text_file in line:
            file_path = os.path.join(os.getenv("WORDBANK_PATH"), text_file + '.txt')
            with open(file_path) as file:
                lines = file.readlines()
                haiku_line.append(lines[random.randrange(len(lines))][:-1])
        haiku.append(' '.join(haiku_line))

    for index, line in enumerate(haiku):
        haiku[index] = line[0].upper()+line[1:]

    return '\n'.join(haiku)


if __name__ == "__main__":
    haiku_text = generate_haiku() + '\n#haiku'
    if len(haiku_text) >= 280:
        exit(1)
    print(haiku_text)
    tweet(generate_haiku() + '\n#haiku')

