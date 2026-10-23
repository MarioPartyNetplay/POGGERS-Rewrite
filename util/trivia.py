import discord
from discord.ext import commands
import random

# 1. Create the Modal (The popup text box)
class TriviaModal(discord.ui.Modal):
    def __init__(self, answer_list, exact_answer, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.answer_list = answer_list
        self.exact_answer = exact_answer

        self.add_item(discord.ui.InputText(
            label="Type your answer below",
            style=discord.InputTextStyle.short,
            placeholder="e.g. Spike",
            required=True
        ))

    async def callback(self, interaction: discord.Interaction):
        # This gets triggered when they hit submit
        user_answer = self.children[0].value.lower()

        # Format the user's answer just like before
        user_answer = user_answer.replace("dk", "kong")
        user_answer = user_answer.replace("twenty one", "21")
        user_answer = user_answer.replace("twentyone", "21")
        user_answer = user_answer.replace("twelve", "12")
        user_answer = user_answer.replace("reversal", "fortune")
        user_answer = user_answer.replace("dd", "drive")
        user_answer = user_answer.replace("two", "2")
        
        # Check if they got it right
        is_correct = any(answer in user_answer for answer in self.answer_list)

        if is_correct:
            await interaction.response.send_message(f"**Correct Answer!** {interaction.user.mention} guessed it right!")
        else:
            await interaction.response.send_message(f"**Wrong Answer!** <:Thwomp:266840621149454348> Correct Answer was **{self.exact_answer}**")

# 2. Create the View (The button attached to the message)
class TriviaView(discord.ui.View):
    def __init__(self, answer_list, exact_answer):
        super().__init__(timeout=60.0) # 60 second timer
        self.answer_list = answer_list
        self.exact_answer = exact_answer

    @discord.ui.button(label="Answer Question", style=discord.ButtonStyle.primary)
    async def answer_button_callback(self, button, interaction: discord.Interaction):
        # Spawn the modal when clicked
        modal = TriviaModal(self.answer_list, self.exact_answer, title="Mario Party IQ")
        await interaction.response.send_modal(modal)
        
        # Disable the button after someone clicks it
        for child in self.children:
            child.disabled = True
        await interaction.message.edit(view=self)
        self.stop()

    async def on_timeout(self):
        # If no one clicks the button in 60 seconds
        for child in self.children:
            child.disabled = True
        # Try to edit the message to show it timed out, if we have a reference
        if self.message:
            await self.message.edit(content=f"**Time is up!** The correct answer was: {self.exact_answer}", view=self)