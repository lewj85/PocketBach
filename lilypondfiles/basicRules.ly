\version "2.16.0"  % necessary for upgrading to future LilyPond versions

% in-line comment syntax
%{ multiple line 
comment syntax %}
% note pitches are always lowercase, so "c" but not "C"

\language "english"  % use "f" for flat, "s" for sharp, ff and ss for doubles
% if not "english" then "is" for sharp, "es" for flat, isis and eses for doubles

%{ note durations are: 1=whole note, 2=half note, 4=quarter note, 8, 16...128
so c4 is a quarter note c, gis16 (or gs16 in "english") is a sixteenth note g#
and r instead of pitch is rest, so r1 is a whole note rest, r2 is a half note rest %}

% sample music
\relative c'  % relative mode always moves to closest note starting at the given pitch
{ 
 % if you don't specify \time it defaults to common time "C"
 \partial 8		% pick-up/upbeat
 g8
 c4 d e f| 		% use | to mark the end of a measure, not necessary but safe
 \time 3/4  		% change time signature
 c8 d [e f g] a |	% beam control, starts 1 note before the [ and ends at ]
 fff16			% white space is irrelevant, can break measures onto different lines
 c8. r16 ess4.. |	% dotted notes with ., double dotted with ..
 c4. r |		% even though r isn't dotted, it repeats the same duration as last 
 f1 e4 d | 		% but notice that you can go beyond a measure if you're not careful
 \numericTimeSignature \time 4/4  % to use "4/4" instead of common time "C"
 r4 r2 r4 |		% can specify rests
 c2 ~ c4 g ~ | g8	% ~ is a tie
 \key ef \major 	% change key signature
 \clef bass		% change clef
 g, g'4 		% raise octave with ' and lower with , and put duration afterward
 \clef treble		% can change clef in middle of measure
 g'' g,, |		% double octaves with ,, and ''
 c'\( c,( d) f\) |	% slur, nested slurs
 e a b bf |		% tonality isn't default, so it will use naturals despite key signature
 << \new Staff c1 >>	% more staves
 g4-> g-. g4.-. g8-.-> |	% articulations: accent -> and staccato -. and both ->-. or -.->
				% dotted staccato must repeat duration integer, not just .-. or -..
 
 % multiple ways to create multiple voices
 % note that voice order should be:
 %  Voice 1: highest
 %  Voice 2: lowest
 %  Voice 3: second highest
 %  Voice 4: second lowest
 %  Voice 5: third highest
 %  Voice 6: third lowest
 %  etc.

 % option #1 only works for identical rhythms
 \new Voice <<
   { e4 f8 d e16 f g8 d4 | e1 }
   { c4 d8 b c16 d e8 d4 | c1 }
 >>

 % option #2 explicitly defines each voice
 \clef bass 
 <<
   \new Voice = "first"
     { \voiceOne r8 r16 g e8. f16 g8[ c,] f e16 d }
   \new Voice= "second"
     { \voiceTwo d16 c d8~ d16 b c8~ c16 b c8~ c16 b8. }
 >>

 % option #3 uses \\
 <<
   { r8 r16 g e8. f16 g8[ c,] f e16 d }
   \\
   { d16 c d8~ d16 b c8~ c16 b c8~ c16 b8. }
 >>

}



