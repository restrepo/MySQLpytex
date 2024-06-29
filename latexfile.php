<?
$latexfile= '\documentclass[%
xcolor=pdftex,dvipsnames,table]{beamer}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%Force pdflatex processing even with "$ latex" (required by arXiv)
\pdfoutput=1
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\mode<presentation>
{
%  \usetheme{Madrid}
  % or ...
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%para revelar texto a aparecer en overlays
  \setbeamercovered{transparent} 
  %\setbeamercovered{invisible}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  \setbeamertemplate{blocks}[rounded][shadow=true]
  \setbeamertemplate{navigation symbols}{}

  \setbeamertemplate{footline}{%\hspace*{.5cm}
    \scriptsize{\phantom{Gg}%\insertauthor 
      \hspace*{50pt} 
      \hfill \insertframenumber
      \hspace*{.5cm}}}

  % or whatever (possibly just delete it)
  %\useoutertheme{shadow} 
}
\usepackage[T1]{fontenc}
\usepackage[latin1]{inputenc}
\usepackage[spanish]{babel}
\spanishdecimal{.}
\usepackage{beamerprosper}
\usepackage{amsmath,amssymb}
\usepackage{graphicx}
\usepackage{mycolors}
\usepackage{pgf}

\setlength{\textwidth}{120 mm}
\setbeamersize{text margin left=10pt,text margin right=10pt}

\newcommand{\widescreen}{
\setlength{\paperwidth}{171 mm}
\setlength{\paperheight}{96 mm}
\setlength{\textwidth}{161 mm}
\setlength{\textheight}{86 mm}
}
\begin{document}
\setbeamertemplate{background}{\includegraphics[width=\paperwidth]{gfifseminars}}
\begin{frame}[plain]
\begin{picture}(320,250)
\put(0,210){
\begin{minipage}[t]{1.0\linewidth}
  \begin{center}
    \textbf{\color{red}\large
'.$title.'}\\\\
    \textbf{\color{blue}\small '.$talknameid.'}\\\\
    \textbf{\color{blue}\scriptsize '.$institution.'}\\\\
    \textbf{\color{blue}\footnotesize{Resumen:}}
  \end{center}
 \end{minipage}
}%
\put(0,140){
  \begin{minipage}[t]{1.0\linewidth}
\footnotesize
'.$abstract.'
\end{minipage}
}
\put(0,0){
  \begin{minipage}[t]{1.0\linewidth}
\parbox{0.2\textwidth}{\textbf{\color{red}\scriptsize Lugar: '.$lugar.'}}\parbox{0.6\textwidth}{\centering{\textbf{\color{red}\scriptsize Fecha: '.$valueday[$weekday].' '.$dia.' de '.$valuemes[$mes].'}}}\parbox{0.2\textwidth}{\raggedleft{\textbf{\color{red}\scriptsize Hora: '.$hora.'}}}%
  \end{minipage}
}%    
\end{picture}

\end{frame}

\end{document}';
?>

