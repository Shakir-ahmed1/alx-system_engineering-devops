# kills a process named killmenow
exec { "kill killmenow":
  command  => 'pkill killmenow',
  provider => shell,
}
