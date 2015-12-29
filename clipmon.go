package main

import (
  "fmt"
  "os/user"
  "strings"
  "regexp"
  "github.com/atotto/clipboard"
  "time"
)

func clip_str_to_path_line(clip_str string) string {
  if(strings.Count(clip_str, "\n") > 1) {
    return ""
  }
  usr, _ := user.Current()
  clip_str = strings.Replace(clip_str, "~", usr.HomeDir, 1)
                         //               file extension
                         //      path            |
                         //       |              |
  re := regexp.MustCompile(`[^\w](/[^@^:^\\^\(]+\.[a-z]{2,3})[^:]{0,9}(line.*?|:)([0-9]+)`)
  match := re.FindStringSubmatch(clip_str)
  if(len(match) > 1) {
    return strings.Join([]string{match[1], match[3]}, ":")
  }
  return ""
}

func main() {
  clip_str := nil
  while(True) {
    break
  }
  line := clip_str_to_path_line("this is /foo.py:30")
  if(line != "") {
    fmt.Println("line:", line)
  }

  clip_str := nil
  for {
    prev_value := clip_str
    clip_str, err := clipboard.ReadAll()
    if prev_value == nil {
      prev_value = clip_str
    }
    if clip_str != prev_value {
      fmt.Println("new value:", clip_str)
      path_line = clip_str_to_path_line(clip_str)
      if path_line {
        fmt.Println("got path_line:", path_line)
        exec.Run("/usr/local/bin/atom", path_line)
      }
    }
    time.Sleep(500 * time.Millisecond)
  }
}
