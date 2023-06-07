# 👉 Day 42 Challenge

"Some trainers have no fear. To them, this is just one more challenge".

1. Create a dictionary to store the details of your, ahem, _MokéBeast_.
2. Ask the user to input the following details: name, type (earth, fire, air, water or spirit), special move, starting HP and starting MP.  For now we're just taking in one set of values for one beast.
3. Output the beast's details.
4. Check the beast's type and change the color of the text accordingly. Fire is red, water is blue, air is white. You decide on the others.

🥳 Extra points for getting all the inputs with just one `input` command and the `split` function.

👉 IMPORTANT INFO - keep a note of where this Repl is, you'll need it in a couple of lessons' time.

Example:

```
👾 MokéBeast - The Non-Copyright Generic Beast Battle Game 👾

Input your beast's name > Brian

Input your beast's type > Earth

Input your beast's special move > Flying bellyflop

Input your beast's staring HP > 50

Input your beast's staring MP > 20

# This text outputs in green
Your beast is called Brian. It is an earth beast with a special move of Flying bellyflop
```

<details> <summary> 💡 Hints </summary>
  
- Start with your dictionary.
- You will need a `for` loop.
- Change the font color for the beast's type by using `if` statements.
- Change font color using `print("\033[XXm", end="")` - replace the XX with a [color code](https://ozzmaker.com/add-colour-to-text-in-python/).
</details>