from difflib import get_close_matches


class CommandEngine:

    def __init__(self):

        self.aliases = {
            "calc": "calculator",
            "terminal": "cmd",
            "command prompt": "cmd",
            "file explorer": "explorer",
        }

        self.verbs = [
            "open",
            "launch",
            "run",
            "start",
            "execute",
        ]

    def normalize(self, prompt: str):

        prompt = prompt.lower().strip()

        # Remove common verbs
        for verb in self.verbs:
            if prompt.startswith(verb):
                prompt = prompt[len(verb):].strip()

        # Remove polite words
        for word in [
            "please",
            "could you",
            "can you",
            "for me",
        ]:
            prompt = prompt.replace(word, "")

        prompt = " ".join(prompt.split())

        return prompt

    def resolve(self, prompt, options):

        prompt = self.normalize(prompt)

        if prompt in self.aliases:
            prompt = self.aliases[prompt]

        match = get_close_matches(
            prompt,
            options,
            n=1,
            cutoff=0.65
        )

        if match:
            return match[0]

        return None