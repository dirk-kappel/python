# Jupyter Notebooks

### Create a new notebook
Select 'New' and then select the kernel that you want (Python 3)

### Command Mode
- Enter Command mode by pressing `esc` key

### Edit Mode
- Edit mode allows you to edit the cell contents (press `enter` key) or just click into it.

### Run all cells
- Select the run in the menu then run all. This will run the code in order.
- You can also select to run all cells above if you want.

### Special commands
`!` will be interpreted as a bash command.

### Magics % and %%
- %  : All commands come from the single line. Called line magics.
- %% : The command comes from the entire cell. Called cell magics. 
- `%lsmagic` will list out  all of the magic commands that we can use.
- `%matplotlib inline` allows matplotlib charts to be displayed inline.
- `%% HTML` allow you render html in the notebook. To embed a youtube video select share then select 'embed' and copy the iframe.
- `%%timeit` time how long it takes to run a command

