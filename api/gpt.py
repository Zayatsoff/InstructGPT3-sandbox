import openai

class GPT:
    def __init__(
        self,
        engine="instruct-davinci-beta",
        max_tokens=200,
        temperature=0.5,
        input_prefix="input: ",
        input_suffix="\n",
        output_prefix="\n",
        output_suffix="\n\n",
        append_output_prefix_to_query=False,
    ):
        self.engine = engine
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.input_prefix = input_prefix
        self.input_suffix = input_suffix
        self.output_prefix = output_prefix
        self.output_suffix = output_suffix
        self.append_output_prefix_to_query = append_output_prefix_to_query

    def get_prime_text(self):
        # Formats all examples to prime the model.
        return "".join([self.format_example(ex) for ex in self.examples.values()])

    def get_instruction_text(self):
        # Formats instruction text to prime the model
        return self.instruction + self.output_suffix

    def craft_query(self, prompt):
        # Creates the query for the API request.
        q = (
            self.get_instruction_text()
            + self.get_prime_text()
            + self.input_prefix
            + prompt
            + self.input_suffix
        )
        if self.append_output_prefix_to_query:
            q = q + self.output_prefix

        return q

    def submit_request(self, prompt):
        # Calls the OpenAI API with the specified parameters.
        response = openai.Completion.create(
            engine=self.engine(),
            prompt=self.craft_query(prompt),
            max_tokens=self.max_tokens(),
            temperature=self.temperature(),
            top_p=1,
            n=1,
            stream=False,
            stop=self.stop,
        )
        return response

    def format_example(self, ex):
        # Formats the input, output pair.
        return (
            self.input_prefix
            + ex.get_input()
            + self.input_suffix
            + self.output_prefix
            + ex.get_output()
            + self.output_suffix
        )
