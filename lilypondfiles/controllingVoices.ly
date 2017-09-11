\version "2.16.0"  % necessary for upgrading to future LilyPond versions

\language "english"

instrumentOne = \relative c' {
  \partcombineApart c2^"apart" e |
  \partcombineAutomatic e2^"auto" e |
  \partcombineChords e'2^"chord" e |
  \partcombineAutomatic c2^"auto" c |
  \partcombineApart c2^"apart" \partcombineChordsOnce e^"chord once" |
  c2 c |
}
instrumentTwo = \relative c' {
  c2 c |
  e2 e |
  a,2 c |
  c2 c' |
  c2 c |
  c2 c |
}

<<
  \new Staff { \instrumentOne }
  \new Staff { \instrumentTwo }
  \new Staff { \partcombine \instrumentOne \instrumentTwo }
>>


