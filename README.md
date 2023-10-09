# Assignment #2

## 1. Reflections

  ### 1.1 Computer Mouse
    - Checking if all the buttons (both main and extra) are working as intented
    - Checking if the scrollwheel works
    - Checking how well the mouse performs on different surfaces (tracking)
    - Checking how many times your can click the mouse before it breaks
    - Checking how comfortable the mouse is
    - Checking if the material of the mouse is durable
      
  ### 1.2 Catastrophic Failure
   In the coastal town of Lumsås in 1982, a fateful missile launch incident occurred due to a software glitch. This event serves as a reminder of the vital role software systems play in our modern world and the potential repercussions of software errors. The Danish Navy's frigate "Peder Skram" was preparing for a NATO exercise at sea. Inexplicably, during a routine missile test, a software malfunction triggered the accidental launch of a 600-kilogram Harpoon missile. The missile's erratic trajectory spared lives but left behind a trail of destruction among unoccupied holiday homes. This incident remains a testament to the need for rigorous software testing and the safeguarding of critical systems against unforeseen software errors.

  Given that this incident was due to a glitch, a simulation test with safety overrides could have been employed as a preventive measure. Prior to any live missile test, a comprehensive simulation scenario could have been created. This scenario should mimic the conditions of a missile launch, including all relevant parameters, coordinates, and inputs.

  A simulation test, in short, is designed to assess how one would react to situations encountered while working and how one would solve problems.
  

## 2. Two Katas

  ### 2.1 String Utility

  ### 2.2 Bowling Game Kata


## 3. Investigation of Tools

  ### 3.1 JUnit 5

  #### @Tag
  Allows you to categorize your test method/classes with a userdefined tag.  
  Useful for selectively running tests based on their categories/tag.
  #### @Disabled
  Makes a test method/class disabled, meaning it won't be executed.
  Useful when you tempoarily skip a test that may be failing/not yet implemented.
  #### @RepeatedTest
  Is used to repeat the execution of a test method x number of times.
  Useful for testing senarios that need to be repeated x amount of times, to ensure stability or even verify random behaviour.
  #### @BeforeEach, @AfterEach
  Both annotations marks methods that are run before and after each test method.
  Useful for initializing resources before each test and then clean them up afterwards.
  #### @BeforeAll, @AfterAll
  Both annotations marks methods that are run once before and after all test methods in a test class.
  Useful for setting up expensive resources that can be shared across multiple methods - such as initializing a database conenction.
  #### @DisplayName
  Allows your to provide a custom name for a test method/class, which is displayed in test reports.
  Useful for providing descriptive names to your test, making it easier to understand the purpose of each test case.
  #### @Nested
  Enables the creation of nested test class with a test class.
  Useful for making a better and organized test code, by grouping related tests together.
  #### @assumeFalse, @assumeTrue
  Allows you to conditionally skip tests based on certain assumptions.
  Useful for controlling test execution, based on assumptions, making tests more flexible to different enviorments.

  ### 3.2 Mocking Frameworks
