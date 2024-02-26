alias my_finder="python3 /Users/vincevasile/Documents/DEV/PYTHON/new_scripts/file_manipulation/copy_and_edit/master_editor.py $@"

sh_runner() {
  script_path=$(findsh $1)
  shift
  bash $script_path $@
}

py_runner() {
  script_path=$(findpy $1)
  shift
  python $script_path $@
}

findsh() {
    script_name=$1
    root_dir=~/documents/DEV/bash
    my_finder -ext sh -find --script "$script_name" -root "$root_dir"
}

findpy() {
    script_name=$1
    root_dir=~/documents/DEV/python
    my_finder -ext py -find --script "$script_name" -root "$root_dir"
}

findzsh() {
    script_name=$1
    root_dir=~/.oh-my-zsh/custom/my_custom_aliases
    my_finder -ext zsh -find --script "$script_name" -root "$root_dir"
}

runsh() {
    script_name=$1
    root_dir=${2:-~/Documents/DEV/bash}
    my_finder -ext sh -run --script "$script_name" -root "$root_dir"
}

runpy() {
    script_name=$1
    root_dir=${2:-~/Documents/DEV/python}
    my_finder -ext py -run --script "$script_name" -root "$root_dir"
}

findandrunsh() {
    script_name=$1
    root_dir=${2:-~/Documents/DEV/bash}
    my_finder -ext sh -run --script "$script_name" -root "$root_dir"
}

copypy() {
    script_name=$1
    root_dir=${2:-~/Documents/DEV/python}
    my_finder -ext py -copy --script "$script_name" -root "$root_dir"
}

copyps1() {
    script_name=$1
    root_dir=${2:-~/Documents/DEV/github/windows_automation}
    my_finder -ext ps1 -copy --script "$script_name" -root "$root_dir"
}

copysh() {
    script_name=$1
    root_dir=${2:-~/Documents/DEV/bash}
    my_finder -ext sh -copy --script "$script_name" -root "$root_dir"
}

listps1() {
    root_dir=${1:-~/Documents/DEV/github/windows_automation}
    my_finder -find -ext ps1 -root "$root_dir"
}

listpy() {
    root_dir=${1:-~/Documents/DEV/python}
    my_finder -find -ext py -root "$root_dir"
}

listsh() {
    root_dir=${1:-~/Documents/DEV/bash}
    my_finder -find -ext sh -root "$root_dir"
}

script_finder() {
  echo "Enter the file extension: "
  read extension
  echo "Enter the directory to start the search in: "
  read directory
  echo "Enter the name or partial name of the script: "
  read script_name
  
  echo "Select the action to perform:"
  echo "1) run"
  echo "2) copy"
  echo "3) edit"
  read action_number
  
  case $action_number in
    1) script_action="-run" ;;
    2) script_action="-copy" ;;
    3) script_action="-edit" ;;
    *) echo "Invalid selection. Please enter 1, 2, or 3."; return ;;
  esac
  
  my_finder -ext "$extension" --script "$script_name" -root "$directory" $script_action
}
