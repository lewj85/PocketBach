\version "2.16.0"

% PocketBach Score by Jesse Lew
\language "english"

\parallelMusic #'(voiceA voiceB voiceC)
{
%soprano
\relative c'' e1 | %1
%alto
\relative f' c1 | %1
%bass
\relative c c1 | %1

%soprano
\relative c'' f1 | %2
%alto
\relative f' a1 | %2
%bass
\relative c c1 | %2

%soprano
\relative c'' g1 | %3
%alto
\relative f' b1 | %3
%bass
\relative c g1 | %3

%soprano
\relative c'' e1 | %4
%alto
\relative f' g1 | %4
%bass
\relative c c1 | %4

%soprano
\relative c'' e1 | %5
%alto
\relative f' c1 | %5
%bass
\relative c a1 | %5

%soprano
\relative c'' e1 | %6
%alto
\relative f' c1 | %6
%bass
\relative c c1 | %6

%soprano
\relative c'' f1 | %7
%alto
\relative f' a1 | %7
%bass
\relative c f1 | %7

%soprano
\relative c'' g1 | %8
%alto
\relative f' b1 | %8
%bass
\relative c g1 | %8

%soprano
\relative c'' c1 | %9
%alto
\relative f' e1 | %9
%bass
\relative c g1 | %9

%soprano
\relative c'' a1 | %10
%alto
\relative f' f1 | %10
%bass
\relative c f1 | %10

%soprano
\relative c'' b1 | %11
%alto
\relative f' d1 | %11
%bass
\relative c g1 | %11

%soprano
\relative c'' c1 | %12
%alto
\relative f' e1 | %12
%bass
\relative c c1 | %12

%soprano
\relative c'' d1 | %13
%alto
\relative f' f1 | %13
%bass
\relative c d1 | %13

%soprano
\relative c'' f1 | %14
%alto
\relative f' d1 | %14
%bass
\relative c d1 | %14

%soprano
\relative c'' g1 | %15
%alto
\relative f' b1 | %15
%bass
\relative c g1 | %15

%soprano
\relative c'' c1 | %16
%alto
\relative f' e1 | %16
%bass
\relative c c1 | %16

}
\new StaffGroup <<
  \new Staff << \relative c'' \voiceA \\ \relative c' \voiceB >>
  \new Staff \relative c { \clef bass \voiceC }
>>