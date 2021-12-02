 function getUrls($urls){
  foreach ($url in $urls){
     echo "Getting URL ${url}"
     $filename = $url.replace("http://")
     $filename = $url.replace("https://")
     curl $url -o "${filename}.html"
     echo "--------------------------------------------"
   }
 }