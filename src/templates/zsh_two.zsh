sh_runner() {
  script_path=$(findsh $1)
  shift
  echo "Running $script_path"
  bash $script_path $@
}

py_runner() {
  script_path=$(findpy $1)
  shift
  echo "Running $script_path"
  python $script_path $@
}
