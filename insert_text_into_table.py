
#The function splits text inte lines of 280 characters each. The function returns a list of lines. The last line may contain less than 280 characters without breaking any word
#It discards the last line
def split_text_into_lines(text):
    lines = []
    for i in range(0, len(text), 280):
        lines.append(text[i:i+280])
    lines.pop()
    return lines

blocks = split_text_into_lines("""
A transistor is a semiconductor device used to amplify or switch electrical signals and power. The transistor is one of the basic building blocks of modern electronics.[1] It is composed of semiconductor material, usually with at least three terminals for connection to an electronic circuit. A voltage or current applied to one pair of the transistor's terminals controls the current through another pair of terminals. Because the controlled (output) power can be higher than the controlling (input) power, a transistor can amplify a signal. Some transistors are packaged individually, but many more in miniature form are found embedded in integrated circuits.

Physicist Julius Edgar Lilienfeld proposed the concept of a field-effect transistor in 1926, but it was not possible to actually construct a working device at that time.[2] The first working device to be built was a point-contact transistor invented in 1947 by physicists John Bardeen and Walter Brattain while working under William Shockley at Bell Labs. The three shared the 1956 Nobel Prize in Physics for their achievement.[3] The most widely used type of transistor is the metal–oxide–semiconductor field-effect transistor (MOSFET), which was invented by Mohamed Atalla and Dawon Kahng at Bell Labs in 1959.[4][5][6] Transistors revolutionized the field of electronics, and paved the way for smaller and cheaper radios, calculators, and computers, among other things.

Most transistors are made from very pure silicon, and some from germanium, but certain other semiconductor materials are sometimes used. A transistor may have only one kind of charge carrier, in a field-effect transistor, or may have two kinds of charge carriers in bipolar junction transistor devices. Compared with the vacuum tube, transistors are generally smaller and require less power to operate. Certain vacuum tubes have advantages over transistors at very high operating frequencies or high operating voltages. Many types of transistors are made to standardized specifications by multiple manufacturers. """)
for i in blocks:
  print(len(i))

def insert_text_into_table(text,tag):
    blocks = split_text_into_lines(text)
    for block in blocks:
      try:
        insert_record("base_blocks","INSERT INTO table_blocks VALUES (NULL,'"+tag+"','"+block+"')")
      except:
        print("Error inserting record")
insert_text_into_table("""1999 	Fred Brooks 	Fred Brooks (cropped).jpg 	For landmark contributions to computer architecture, operating systems, and software engineering. 	IBM,
University of North Carolina at Chapel Hill
2000 	Andrew Yao 	Andrew Yao MFO (cropped).jpg 	In recognition of his fundamental contributions to the theory of computation, including the complexity-based theory of pseudorandom number generation, cryptography, and communication complexity. 	Stanford University,
University of California, Berkeley,
Princeton University
2001 	Ole-Johan Dahl 		For ideas fundamental to the emergence of object-oriented programming, through their design of the programming languages Simula I and Simula 67. 	Norwegian Computing Center
Kristen Nygaard 	Kristen-Nygaard-SBLP-1997-head.png
2002 	Ron Rivest 	Ronald L Rivest photo.jpg 	For their ingenious contribution for making public-key cryptography useful in practice. 	Massachusetts Institute of Technology
Adi Shamir 	Adi Shamir at TU Darmstadt (2013).jpg
Leonard Adleman 	Len-mankin-pic.jpg 	University of Southern California
2003 	Alan Kay 	Alan Kay (3097597186) (cropped).jpg 	For pioneering many of the ideas at the root of contemporary object-oriented programming languages, leading the team that developed Smalltalk, and for fundamental contributions to personal computing. 	University of Utah,
PARC,
Stanford University,
Atari,
Apple ATG,
Walt Disney Imagineering,
Viewpoints Research Institute,
HP Labs
2004 	Vint Cerf 	Dr Vint Cerf ForMemRS (cropped).jpg 	For pioneering work on internetworking, including the design and implementation of the Internet's basic communications protocols, TCP/IP, and for inspired leadership in networking. 	University of California, Los Angeles,
Stanford University, DARPA,
MCI (now under Verizon),
CNRI, Google
Bob Kahn 	Bob Kahn.jpg 	MIT,
Bolt Beranek and Newman,
DARPA,
CNRI
2005 	Peter Naur 	Peternaur.JPG 	For fundamental contributions to programming language design and the definition of ALGOL 60, to compiler design, and to the art and practice of computer programming. 	Regnecentralen (now under Fujitsu),
University of Copenhagen
2006 	Frances Allen 	Allen mg 2528-3750K-b.jpg 	For pioneering contributions to the theory and practice of optimizing compiler techniques that laid the foundation for modern optimizing compilers and automatic parallel execution. 	IBM
2007 	Edmund M. Clarke 	Edmund Clarke FLoC 2006 (cropped).jpg 	For their roles in developing model checking into a highly effective verification technology, widely adopted in the hardware and software industries.[38] 	Harvard University,
Carnegie Mellon University
E. Allen Emerson 	E-allen-emerson (cropped).jpg 	Harvard University
Joseph Sifakis 	Joseph Sifakis img 0966.jpg 	French National Centre for Scientific Research
2008 	Barbara Liskov 	Barbara Liskov MIT computer scientist 2010.jpg 	For contributions to practical and theoretical foundations of programming language and system design, especially related to data abstraction, fault tolerance, and distributed computing. 	Massachusetts Institute of Technology
2009 	Charles P. Thacker 	Chuckthacker (cropped).jpg 	For his pioneering design and realization of the Xerox Alto, the first modern personal computer, and in addition for his contributions to the Ethernet and the Tablet PC. 	PARC,
DEC,
Microsoft Research
2010 	Leslie Valiant 	Leslie Valiant (cropped).jpg 	For transformative contributions to the theory of computation, including the theory of probably approximately correct (PAC) learning, the complexity of enumeration and of algebraic computation, and the theory of parallel and distributed computing. 	Harvard University
2011 	Judea Pearl[39] 	Judea Pearl at NIPS 2013 (11781981594) (cropped).jpg 	For fundamental contributions to artificial intelligence through the development of a calculus for probabilistic and causal reasoning.[40] 	University of California, Los Angeles
New Jersey Institute of Technology
2012 	Silvio Micali 	Silvio Micali (cropped).jpg 	For transformative work that laid the complexity-theoretic foundations for the science of cryptography and in the process pioneered new methods for efficient verification of mathematical proofs in complexity theory.[41] 	Massachusetts Institute of Technology
Shafi Goldwasser 	Shafi Goldwasser.JPG 	Massachusetts Institute of Technology,
Weizmann Institute of Science
2013 	Leslie Lamport 	Leslie Lamport.jpg 	For fundamental contributions to the theory and practice of distributed and concurrent systems, notably the invention of concepts such as causality and logical clocks, safety and liveness, replicated state machines, and sequential consistency.[42][43] 	Massachusetts Computer Associates (now under Essig PLM),
SRI International,
""","turing_award")
