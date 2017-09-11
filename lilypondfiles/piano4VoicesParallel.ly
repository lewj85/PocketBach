\version "2.16.0"  % necessary for upgrading to future LilyPond versions

\language "english"

global = {
  \key c \major
  \time 2/4
}

\parallelMusic #'(voiceA voiceB voiceC voiceD) {
  % Bar 1
  a8    b     c   d     |
  d4          e         |
  c16 d e f   d e f g   |
  a4          a         |

  % Bar 2
  e8    f    g   a     |
  f4         g         |
  e16 f g a  f g a b   |
  a4         a         |

  % Bar 3 ...
}

\score {
  \new PianoStaff <<
     \new Staff {
       \global
       <<
         \relative c'' \voiceA
         \\
         \relative c'  \voiceB
       >>
     }
     \new Staff {
       \global \clef bass
       <<
         \relative c \voiceC
         \\
         \relative c \voiceD
       >>
     }
  >>
}