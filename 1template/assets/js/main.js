/***************************************************
==================== JS INDEX ======================
****************************************************
01. PreLoader Js
02. Mobile Menu Js
03. Common Js
04. Menu Controls JS
05. Offcanvas Js
06. Search Js
07. cartmini Js
08. filter
09. Body overlay Js
10. Sticky Header Js
11. Theme Settings Js
12. Nice Select Js
13. Smooth Scroll Js
14. Slider Activation Area Start
15. Masonary Js
16. Wow Js
17. Counter Js
18. InHover Active Js
19. Line Animation Js
20. Video Play Js
21. Password Toggle Js
****************************************************/

(function ($) {
	"use strict";

	var windowOn = $(window);
	////////////////////////////////////////////////////
	// 01. PreLoader Js
	windowOn.on('load', function () {
		$("#loading").fadeOut(500);
	});


	////////////////////////////////////////////////////
	// 02. Mobile Menu Js
	$('#mobile-menu').meanmenu({
		meanMenuContainer: '.mobile-menu',
		meanScreenWidth: "991",
		meanExpand: ['<i class="fa-regular fa-angle-right"></i>'],
	});

	$('#mobile-menu-lg').meanmenu({
		meanMenuContainer: '.mobile-menu-lg',
		meanScreenWidth: "1199",
		meanExpand: ['<i class="fa-regular fa-angle-right"></i>'],
	});

	////////////////////////////////////////////////////
	// 03. Common Js

	$("[data-background").each(function () {
		$(this).css("background-image", "url( " + $(this).attr("data-background") + "  )");
	});

	$("[data-width]").each(function () {
		$(this).css("width", $(this).attr("data-width"));
	});

	$("[data-bg-color]").each(function () {
		$(this).css("background-color", $(this).attr("data-bg-color"));
	});

	$("[data-text-color]").each(function () {
		$(this).css("color", $(this).attr("data-text-color"));
	});

	$(".has-img").each(function () {
		var imgSrc = $(this).attr("data-menu-img");
		var img = `<img class="mega-menu-img" src="${imgSrc}" alt="img">`;
		$(this).append(img);

	});


	$('.wp-menu nav > ul > li').slice(-4).addClass('menu-last');

	$('.aakriticm-header-side-menu > nav > ul > li a, .offcanvas__category > nav > ul > li a').each(function(i, v) {
		$(v).contents().eq(2).wrap('<span class="menu-text"/>');
	});


	if($('.main-menu.menu-style-3 > nav > ul').length > 0){
		$('.main-menu.menu-style-3 > nav > ul').append(`<li id="marker" class="aakriticm-menu-line"></li>`);
	}

	if ($("#aakriticm-offcanvas-lang-toggle").length > 0) {
		window.addEventListener('click', function(e){
		
			if (document.getElementById('aakriticm-offcanvas-lang-toggle').contains(e.target)){
				$(".aakriticm-lang-list").toggleClass("aakriticm-lang-list-open");
			}
			else{
				$(".aakriticm-lang-list").removeClass("aakriticm-lang-list-open");
			}
		});
	}

	if ($("#aakriticm-offcanvas-currency-toggle").length > 0) {
		window.addEventListener('click', function(e){
		
			if (document.getElementById('aakriticm-offcanvas-currency-toggle').contains(e.target)){
				$(".aakriticm-currency-list").toggleClass("aakriticm-currency-list-open");
			}
			else{
				$(".aakriticm-currency-list").removeClass("aakriticm-currency-list-open");
			}
		});
	}

	// for header language
	if ($("#aakriticm-header-lang-toggle").length > 0) {
		window.addEventListener('click', function(e){
	
			if (document.getElementById('aakriticm-header-lang-toggle').contains(e.target)){
				$(".aakriticm-header-lang ul").toggleClass("aakriticm-lang-list-open");
			}
			else{
				$(".aakriticm-header-lang ul").removeClass("aakriticm-lang-list-open");
			}
		});
	}

	// for header currency
	if ($("#aakriticm-header-currency-toggle").length > 0) {
		window.addEventListener('click', function(e){
	
			if (document.getElementById('aakriticm-header-currency-toggle').contains(e.target)){
				$(".aakriticm-header-currency ul").toggleClass("aakriticm-currency-list-open");
			}
			else{
				$(".aakriticm-header-currency ul").removeClass("aakriticm-currency-list-open");
			}
		});
	}

	// for header setting
	if ($("#aakriticm-header-setting-toggle").length > 0) {
		window.addEventListener('click', function(e){
	
			if (document.getElementById('aakriticm-header-setting-toggle').contains(e.target)){
				$(".aakriticm-header-setting ul").toggleClass("aakriticm-setting-list-open");
			}
			else{
				$(".aakriticm-header-setting ul").removeClass("aakriticm-setting-list-open");
			}
		});
	}

	$('.aakriticm-hamburger-toggle').on('click', function(){
		$('.aakriticm-header-side-menu').slideToggle('aakriticm-header-side-menu');
	});


	////////////////////////////////////////////////////
	// 04. Menu Controls JS
	if($('.aakriticm-category-menu-content').length && $('.aakriticm-category-mobile-menu').length){
		let navContent = document.querySelector(".aakriticm-category-menu-content").outerHTML;
		let mobileNavContainer = document.querySelector(".aakriticm-category-mobile-menu");
		mobileNavContainer.innerHTML = navContent;
	
		$('.aakriticm-offcanvas-category-toggle').on('click', function(){
			$(this).siblings().find('nav').slideToggle();
		});
		
	
		let arrow = $(".aakriticm-category-mobile-menu .has-dropdown > a");
	
		arrow.each(function () {
			let self = $(this);
			let arrowBtn = document.createElement("BUTTON");
			arrowBtn.classList.add("dropdown-toggle-btn");
			arrowBtn.innerHTML = "<i class='fa-regular fa-angle-right'></i>";
	
			self.append(function () {
			  return arrowBtn;
			});
	
			self.find("button").on("click", function (e) {
			  e.preventDefault();
			  let self = $(this);
			  self.toggleClass("dropdown-opened");
			  self.parent().toggleClass("expanded");
			  self.parent().parent().addClass("dropdown-opened").siblings().removeClass("dropdown-opened");
			  self.parent().parent().children(".aakriticm-submenu").slideToggle();
			  
	
			});
	
		  });
	}

	if($('.aakriticm-main-menu-content').length && $('.aakriticm-main-menu-mobile').length){
		let navContent = document.querySelector(".aakriticm-main-menu-content").outerHTML;
		let mobileNavContainer = document.querySelector(".aakriticm-main-menu-mobile");
		mobileNavContainer.innerHTML = navContent;
	
	
		let arrow = $(".aakriticm-main-menu-mobile .has-dropdown > a");
	
		arrow.each(function () {
			let self = $(this);
			let arrowBtn = document.createElement("BUTTON");
			arrowBtn.classList.add("dropdown-toggle-btn");
			arrowBtn.innerHTML = "<i class='fa-regular fa-angle-right'></i>";
	
			self.append(function () {
			  return arrowBtn;
			});
	
			self.find("button").on("click", function (e) {
			  e.preventDefault();
			  let self = $(this);
			  self.toggleClass("dropdown-opened");
			  self.parent().toggleClass("expanded");
			  self.parent().parent().addClass("dropdown-opened").siblings().removeClass("dropdown-opened");
			  self.parent().parent().children(".aakriticm-submenu").slideToggle();
			  
	
			});
	
		  });
	}

	$(".aakriticm-category-menu-toggle").on("click", function () {
		$(".aakriticm-category-menu > nav > ul").slideToggle();
	});



	////////////////////////////////////////////////////
	// 05. Offcanvas Js
	$(".aakriticm-offcanvas-open-btn").on("click", function () {
		$(".offcanvas__area").addClass("offcanvas-opened");
		$(".body-overlay").addClass("opened");
	});
	$(".offcanvas-close-btn").on("click", function () {
		$(".offcanvas__area").removeClass("offcanvas-opened");
		$(".body-overlay").removeClass("opened");
	});

	////////////////////////////////////////////////////
	// 06. Search Js
	$(".aakriticm-search-open-btn").on("click", function () {
		$(".aakriticm-search-area").addClass("opened");
		$(".body-overlay").addClass("opened");
	});
	$(".aakriticm-search-close-btn").on("click", function () {
		$(".aakriticm-search-area").removeClass("opened");
		$(".body-overlay").removeClass("opened");
	});

	////////////////////////////////////////////////////
	// 07. cartmini Js
	$(".cartmini-open-btn").on("click", function () {
		$(".cartmini__area").addClass("cartmini-opened");
		$(".body-overlay").addClass("opened");
	});


	$(".cartmini-close-btn").on("click", function () {
		$(".cartmini__area").removeClass("cartmini-opened");
		$(".body-overlay").removeClass("opened");
	});

	////////////////////////////////////////////////////
	// 08. filter
	$(".filter-open-btn").on("click", function () {
		$(".aakriticm-filter-offcanvas-area").addClass("offcanvas-opened");
		$(".body-overlay").addClass("opened");
	});


	$(".filter-close-btn").on("click", function () {
		$(".aakriticm-filter-offcanvas-area").removeClass("offcanvas-opened");
		$(".body-overlay").removeClass("opened");
	});

	$(".filter-open-dropdown-btn").on("click", function () {
		$(".aakriticm-filter-dropdown-area").toggleClass('filter-dropdown-opened');
	});


	////////////////////////////////////////////////////
	// 09. Body overlay Js
	$(".body-overlay").on("click", function () {
		$(".offcanvas__area").removeClass("offcanvas-opened");
		$(".aakriticm-search-area").removeClass("opened");
		$(".cartmini__area").removeClass("cartmini-opened");
		$(".aakriticm-filter-offcanvas-area").removeClass("offcanvas-opened");
		$(".body-overlay").removeClass("opened");
	});


	////////////////////////////////////////////////////
	// 10. Sticky Header Js
	windowOn.on('scroll', function () {
		var scroll = $(window).scrollTop();
		if (scroll < 100) {
			$("#header-sticky").removeClass("header-sticky");
			$("#header-sticky-2").removeClass("header-sticky-2");
		} else {
			$("#header-sticky").addClass("header-sticky");
			$("#header-sticky-2").addClass("header-sticky-2");
		}
	});

	windowOn.on('scroll', function () {
		var scroll = $(window).scrollTop();
		if (scroll < 100) {
			$(".aakriticm-side-menu-5").removeClass("sticky-active");
		} else {
			$(".aakriticm-side-menu-5").addClass("sticky-active");
		}
	});




	////////////////////////////////////////////////////
	// 11. Theme Settings Js

	// settings append in body
	function tp_settings_append($x){
		var settings = $('body');
		let dark;
		$x == true ? dark = 'd-block' : dark = 'd-none';
		var settings_html = `<div class="aakriticm-theme-settings-area transition-3">
		<div class="aakriticm-theme-wrapper">
		   <div class="aakriticm-theme-header text-center">
			  <h4 class="aakriticm-theme-header-title">Harry Theme Settings</h4>
		   </div>

		   <!-- THEME TOGGLER -->
		   <div class="aakriticm-theme-toggle mb-20 ${dark}">
			  <label class="aakriticm-theme-toggle-main" for="aakriticm-theme-toggler">
				 <span class="aakriticm-theme-toggle-dark"><i class="fa-light fa-moon"></i> Dark</span>
					<input type="checkbox" id="aakriticm-theme-toggler">
					<i class="aakriticm-theme-toggle-slide"></i>
				 <span class="aakriticm-theme-toggle-light active"><i class="fa-light fa-sun-bright"></i> Light</span>
			  </label>
		   </div>

		   <!--  RTL SETTINGS -->
		   <div class="aakriticm-theme-dir mb-20">
			  <label class="aakriticm-theme-dir-main" for="aakriticm-dir-toggler">
				 <span class="aakriticm-theme-dir-rtl"> RTL</span>
					<input type="checkbox" id="aakriticm-dir-toggler">
					<i class="aakriticm-theme-dir-slide"></i>
				 <span class="aakriticm-theme-dir-ltr active"> LTR</span>
			  </label>
		   </div>

		   <!-- COLOR SETTINGS -->
		   <div class="aakriticm-theme-settings">
			  <div class="aakriticm-theme-settings-wrapper">
				 <div class="aakriticm-theme-settings-open">
					<button class="aakriticm-theme-settings-open-btn">
					   <span class="aakriticm-theme-settings-gear">
						  <i class="fa-light fa-gear"></i>
					   </span>
					   <span class="aakriticm-theme-settings-close">
						  <i class="fa-regular fa-xmark"></i>
					   </span>
					</button>
				 </div>
				 <div class="row row-cols-4 gy-2 gx-2">
					<div class="col">
					   <div class="aakriticm-theme-color-item aakriticm-color-active">
						  <button class="aakriticm-theme-color-btn aakriticm-color-settings-btn d-none" data-color-default="#F50963" type="button" data-color="#F50963"></button>
						  <button class="aakriticm-theme-color-btn aakriticm-color-settings-btn" type="button" data-color="#F50963"></button>
					   </div>
					</div>
					<div class="col">
					   <div class="aakriticm-theme-color-item aakriticm-color-active">
						  <button class="aakriticm-theme-color-btn aakriticm-color-settings-btn" type="button" data-color="#008080"></button>
					   </div>
					</div>
					<div class="col">
					   <div class="aakriticm-theme-color-item aakriticm-color-active">
						  <button class="aakriticm-theme-color-btn aakriticm-color-settings-btn" type="button" data-color="#AB6C56"></button>
					   </div>
					</div>
					<div class="col">
					   <div class="aakriticm-theme-color-item aakriticm-color-active">
						  <button class="aakriticm-theme-color-btn aakriticm-color-settings-btn" type="button" data-color="#3661FC"></button>
					   </div>
					</div>
					<div class="col">
					   <div class="aakriticm-theme-color-item aakriticm-color-active">
						  <button class="aakriticm-theme-color-btn aakriticm-color-settings-btn" type="button" data-color="#2CAE76"></button>
					   </div>
					</div>
					<div class="col">
					   <div class="aakriticm-theme-color-item aakriticm-color-active">
						  <button class="aakriticm-theme-color-btn aakriticm-color-settings-btn" type="button" data-color="#FF5A1B"></button>
					   </div>
					</div>
					<div class="col">
                        <div class="aakriticm-theme-color-item aakriticm-color-active">
                           <button class="aakriticm-theme-color-btn aakriticm-color-settings-btn" type="button" data-color="#03041C"></button>
                        </div>
                     </div>
					<div class="col">
					   <div class="aakriticm-theme-color-item aakriticm-color-active">
						  <button class="aakriticm-theme-color-btn aakriticm-color-settings-btn" type="button" data-color="#ED212C"></button>
					   </div>
					</div>
				 </div>
			  </div>
			  <div class="aakriticm-theme-color-input">
				 <h6>Choose Custom Color</h6>
				 <input type="color" id="aakriticm-color-setings-input" value="#F50963">
				 <label id="aakriticm-theme-color-label" for="aakriticm-color-setings-input"></label>
			  </div>
		   </div>
		</div>
	 </div>`;
	 settings.append(settings_html);
	}
	// tp_settings_append(true); // if want to enable dark light mode then send "true";

	// settings open btn
	$(".aakriticm-theme-settings-open-btn").on("click", function () {
		$(".aakriticm-theme-settings-area").toggleClass("settings-opened");
	});

	// rtl settings
	function tp_rtl_settings() {

		$('#aakriticm-dir-toggler').on("change", function () {
			toggle_rtl();

		});


		// set toggle theme scheme
		function tp_set_scheme(tp_dir) {
			localStorage.setItem('tp_dir', tp_dir);
			document.documentElement.setAttribute("dir", tp_dir);

			if (tp_dir === 'rtl') {
				var list = $("[href='assets/css/bootstrap.css']");
				$(list).attr("href", "assets/css/bootstrap-rtl.css");
			} else {
				var list = $("[href='assets/css/bootstrap.css']");
				$(list).attr("href", "assets/css/bootstrap.css");
			}
		}

		// toogle theme scheme
		function toggle_rtl() {
			if (localStorage.getItem('tp_dir') === 'rtl') {
				tp_set_scheme('ltr');
				var list = $("[href='assets/css/bootstrap-rtl.css']");
				$(list).attr("href", "assets/css/bootstrap.css");
			} else {
				tp_set_scheme('rtl');
				var list = $("[href='assets/css/bootstrap.css']");
				$(list).attr("href", "assets/css/bootstrap-rtl.css");
			}
		}

		// set the first theme scheme
		function tp_init_dir() {
			if (localStorage.getItem('tp_dir') === 'rtl') {
				tp_set_scheme('rtl');
				var list = $("[href='assets/css/bootstrap.css']");
				$(list).attr("href", "assets/css/bootstrap-rtl.css");
				document.getElementById('aakriticm-dir-toggler').checked = true;
			} else {
				tp_set_scheme('ltr');
				document.getElementById('aakriticm-dir-toggler').checked = false;
				var list = $("[href='assets/css/bootstrap.css']");
				$(list).attr("href", "assets/css/bootstrap.css");
			}
		}
		tp_init_dir();
	}
	if ($("#aakriticm-dir-toggler").length > 0) {
		tp_rtl_settings();
	}

	// dark light mode toggler
	function tp_theme_toggler() {

		$('#aakriticm-theme-toggler').on("change", function () {
			toggleTheme();

		});


		// set toggle theme scheme
		function tp_set_scheme(tp_theme) {
			localStorage.setItem('tp_theme_scheme', tp_theme);
			document.documentElement.setAttribute("aakriticm-theme", tp_theme);
		}

		// toogle theme scheme
		function toggleTheme() {
			if (localStorage.getItem('tp_theme_scheme') === 'aakriticm-theme-dark') {
				tp_set_scheme('aakriticm-theme-light');
			} else {
				tp_set_scheme('aakriticm-theme-dark');
			}
		}

		// set the first theme scheme
		function tp_init_theme() {
			if (localStorage.getItem('tp_theme_scheme') === 'aakriticm-theme-dark') {
				tp_set_scheme('aakriticm-theme-dark');
				document.getElementById('aakriticm-theme-toggler').checked = true;
			} else {
				tp_set_scheme('aakriticm-theme-light');
				document.getElementById('aakriticm-theme-toggler').checked = false;
			}
		}
		tp_init_theme();
	}
	if ($("#aakriticm-theme-toggler").length > 0) {
		tp_theme_toggler();
	}


	// color settings
	function tp_color_settings() {

		// set color scheme
		function tp_set_color(tp_color_scheme) {
			localStorage.setItem('tp_color_scheme', tp_color_scheme);
			document.querySelector(':root').style.setProperty('--aakriticm-theme-1', tp_color_scheme);
			document.getElementById("aakriticm-color-setings-input").value = tp_color_scheme;
			document.getElementById("aakriticm-theme-color-label").style.backgroundColor = tp_color_scheme;
		}

		// set color
		function tp_set_input() {
			var color = localStorage.getItem('tp_color_scheme');
			document.getElementById("aakriticm-color-setings-input").value = color;
			document.getElementById("aakriticm-theme-color-label").style.backgroundColor = color;


		}
		tp_set_input();

		function tp_init_color() {
			var defaultColor = $(".aakriticm-color-settings-btn").attr('data-color-default');
			var setColor = localStorage.getItem('tp_color_scheme');

			if (setColor != null) {

			} else {
				setColor = defaultColor;
			}

			if (defaultColor !== setColor) {
				document.querySelector(':root').style.setProperty('--aakriticm-theme-1', setColor);
				document.getElementById("aakriticm-color-setings-input").value = setColor;
				document.getElementById("aakriticm-theme-color-label").style.backgroundColor = setColor;
				tp_set_color(setColor);
			} else {
				document.querySelector(':root').style.setProperty('--aakriticm-theme-1', defaultColor);
				document.getElementById("aakriticm-color-setings-input").value = defaultColor;
				document.getElementById("aakriticm-theme-color-label").style.backgroundColor = defaultColor;
				tp_set_color(defaultColor);
			}
		}
		tp_init_color();


		let themeButtons = document.querySelectorAll('.aakriticm-color-settings-btn');

		themeButtons.forEach(color => {
			color.addEventListener('click', () => {
				let datacolor = color.getAttribute('data-color');
				document.querySelector(':root').style.setProperty('--aakriticm-theme-1', datacolor);
				document.getElementById("aakriticm-theme-color-label").style.backgroundColor = datacolor;
				tp_set_color(datacolor);
			});
		});



		const colorInput = document.querySelector('#aakriticm-color-setings-input');
		const colorVariable = '--aakriticm-theme-1';


		colorInput.addEventListener('change', function (e) {
			var clr = e.target.value;
			document.documentElement.style.setProperty(colorVariable, clr);
			tp_set_color(clr);
			tp_set_check(clr);
		});


		function tp_set_check(clr){
			const arr = Array.from(document.querySelectorAll('[data-color]'));
	
			var a = localStorage.getItem('tp_color_scheme');

			let test =  arr.map(color =>{
				let datacolor = color.getAttribute('data-color');
				
				return datacolor;
			}).filter(color => color == a);
			
			var arrLength = test.length;

			if(arrLength == 0){
				$('.aakriticm-color-active').removeClass('active');
			}else{
				$('.aakriticm-color-active').addClass('active');
			}
		}

		function tp_check_color(){
			var a = localStorage.getItem('tp_color_scheme');

			var list = $(`[data-color="${a}"]`);

			list.parent().addClass('active').parent().siblings().find('.aakriticm-color-active').removeClass('active')		
		}
		tp_check_color();

		$('.aakriticm-color-active').on('click', function () {
			$(this).addClass('active').parent().siblings().find('.aakriticm-color-active').removeClass('active');
		});

	}
	if (($(".aakriticm-color-settings-btn").length > 0) && ($("#aakriticm-color-setings-input").length > 0) && ($("#aakriticm-theme-color-label").length > 0)) {
		tp_color_settings();
	}



	////////////////////////////////////////////////////
	// 12. Nice Select Js
	$('.aakriticm-header-search-category select, .aakriticm-shop-area select, .aakriticm-checkout-area select, .profile__area select').niceSelect();

	////////////////////////////////////////////////////
	// 13. Smooth Scroll Js
	function smoothSctoll() {
		$('.smooth a').on('click', function (event) {
			var target = $(this.getAttribute('href'));
			if (target.length) {
				event.preventDefault();
				$('html, body').stop().animate({
					scrollTop: target.offset().top - 120
				}, 1500);
			}
		});
	}
	smoothSctoll();

	function back_to_top() {
		var btn = $('#back_to_top');
		var btn_wrapper = $('.back-to-top-wrapper');

		windowOn.scroll(function () {
			if (windowOn.scrollTop() > 300) {
				btn_wrapper.addClass('back-to-top-btn-show');
			} else {
				btn_wrapper.removeClass('back-to-top-btn-show');
			}
		});

		btn.on('click', function (e) {
			e.preventDefault();
			$('html, body').animate({ scrollTop: 0 }, '300');
		});
	}
	back_to_top();

	var tp_rtl = localStorage.getItem('tp_dir');
	let rtl_setting = tp_rtl == 'rtl' ? true : false;

	
	////////////////////////////////////////////////////
	// 14. Slider Activation Area Start
	$('.aakriticm-slider-active-4').slick({
		infinite: true,
		slidesToShow: 1,
		slidesToScroll: 1,
		arrows: true,
		fade: true,
		centerMode: true,
		prevArrow: `<button type="button" class="aakriticm-slider-3-button-prev"><svg width="16" height="14" viewBox="0 0 16 14" fill="none" xmlns="http://www.w3.org/2000/svg">
		   <path d="M1.00073 6.99989L15 6.99989" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
		   <path d="M6.64648 1.5L1.00011 6.99954L6.64648 12.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></button>`,
		nextArrow: `<button type="button" class="aakriticm-slider-3-button-next"><svg width="16" height="14" viewBox="0 0 16 14" fill="none" xmlns="http://www.w3.org/2000/svg">
		<path d="M14.9993 6.99989L1 6.99989" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
		<path d="M9.35352 1.5L14.9999 6.99954L9.35352 12.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
		</svg></button>`,
		asNavFor: '.aakriticm-slider-nav-active',
		appendArrows: $('.aakriticm-slider-arrow-4'),
		
	});

	$('.aakriticm-slider-nav-active').slick({
		infinite: true,
		slidesToShow: 3,
		slidesToScroll: 1,
		vertical: true,
		asNavFor: '.aakriticm-slider-active-4',
		dots: false,
		arrows: false,
		prevArrow: '<button type="button" class="aakriticm-slick-prev"><i class="fa-solid fa-arrow-up"></i></button>',
		nextArrow: '<button type="button" class="aakriticm-slick-next"><i class="fa-solid fa-arrow-down"></i></button>',
		centerMode: false,
		focusOnSelect: true,
	});


	// home electronics
	var mainSlider = new Swiper('.aakriticm-slider-active', {
		slidesPerView: 1,
		spaceBetween: 30,
		loop: true,
		rtl: rtl_setting,
		effect : 'fade',
		// Navigation arrows
		navigation: {
			nextEl: ".aakriticm-slider-button-next",
			prevEl: ".aakriticm-slider-button-prev",
		},
		pagination: {
			el: ".aakriticm-slider-dot",
			clickable: true,
			renderBullet: function (index, className) {
				return '<span class="' + className + '">' + '<button>' + (index + 1) + '</button>' + "</span>";
			},
		},
	});

	mainSlider.on('slideChangeTransitionStart', function (realIndex) {
        if ($('.swiper-slide.swiper-slide-active, .aakriticm-slider-item .is-light').hasClass('is-light')) {
            $('.aakriticm-slider-variation').addClass('is-light');
        } else {
            $('.aakriticm-slider-variation').removeClass('is-light');
        }
    });

	// home electronics
	var slider = new Swiper('.shop-mega-menu-slider-active', {
		slidesPerView: 3,
		spaceBetween: 20,
		loop: true,
		rtl: rtl_setting,
		// Navigation arrows
		navigation: {
			nextEl: ".aakriticm-shop-mega-menu-button-next",
			prevEl: ".aakriticm-shop-mega-menu-button-prev",
		},
		pagination: {
			el: ".aakriticm-shop-mega-menu-dot",
			clickable: true,
			renderBullet: function (index, className) {
				return '<span class="' + className + '">' + '<button>' + (index + 1) + '</button>' + "</span>";
			},
		},
	});

	// home electronics
	var slider = new Swiper('.aakriticm-blog-main-slider-active', {
		slidesPerView: 3,
		spaceBetween: 20,
		loop: true,
		autoplay: {
			delay: 4000,
		  },
		rtl: rtl_setting,
		// Navigation arrows
		navigation: {
			nextEl: ".aakriticm-blog-main-slider-button-next",
			prevEl: ".aakriticm-blog-main-slider-button-prev",
		},
		pagination: {
			el: ".aakriticm-blog-main-slider-dot",
			clickable: true,
			renderBullet: function (index, className) {
				return '<span class="' + className + '">' + '<button>' + (index + 1) + '</button>' + "</span>";
			},
		},
		breakpoints: {
			'1200': {
				slidesPerView: 3,
			},
			'992': {
				slidesPerView: 2,
			},
			'768': {
				slidesPerView: 2,
			},
			'576': {
				slidesPerView: 1,
			},
			'0': {
				slidesPerView: 1,
			},
		},
	});

	// home 2 fashion
	var slider = new Swiper('.aakriticm-slider-active-2', {
		slidesPerView: 1,
		spaceBetween: 30,
		loop: true,
		rtl: rtl_setting,
		effect: 'fade',
		// Navigation arrows
		navigation: {
			nextEl: ".aakriticm-slider-2-button-next",
			prevEl: ".aakriticm-slider-2-button-prev",
		},
		pagination: {
			el: ".aakriticm-slider-2-dot",
			clickable: true,
			renderBullet: function (index, className) {
				return '<span class="' + className + '">' + '<button>' + (index + 1) + '</button>' + "</span>";
			},
		},
	});

	// home 3 beauti
	var slider = new Swiper('.aakriticm-slider-active-3', {
		slidesPerView: 1,
		spaceBetween: 30,
		loop: true,
		rtl: rtl_setting,
		effect: 'fade',
		// Navigation arrows
		navigation: {
			nextEl: ".aakriticm-slider-3-button-next",
			prevEl: ".aakriticm-slider-3-button-prev",
		},
		pagination: {
			el: ".aakriticm-slider-3-dot",
			clickable: true,
			renderBullet: function (index, className) {
				return '<span class="' + className + '">' + '<button>' + (index + 1) + '</button>' + "</span>";
			},
		},
	});

	// home 3 beauti
	var slider = new Swiper('.aakriticm-slider-active-5', {
		slidesPerView: 1,
		spaceBetween: 30,
		loop: true,
		rtl: rtl_setting,
		effect: 'fade',
		// Navigation arrows
		navigation: {
			nextEl: ".aakriticm-slider-5-button-next",
			prevEl: ".aakriticm-slider-5-button-prev",
		},
		pagination: {
			el: ".aakriticm-slider-5-dot",
			clickable: true,
			renderBullet: function (index, className) {
				return '<span class="' + className + '">' + '<button>' + (index + 1) + '</button>' + "</span>";
			},
		},
	});

	var mainSliderThumb4 = new Swiper ('.aakriticm-slider-nav-actives', {
		slidesPerView: 3,
		spaceBetween: 20,
		loop: true,
		direction: 'vertical',
	});

	// home 3 beauti
	var mainSlider4 = new Swiper('.aakriticm-slider-active-4s', {
		slidesPerView: 1,
		spaceBetween: 30,
		loop: true,
		rtl: rtl_setting,
		effect: 'fade',
		// Navigation arrows
		navigation: {
			nextEl: ".aakriticm-slider-3-button-next",
			prevEl: ".aakriticm-slider-3-button-prev",
		},
		pagination: {
			el: ".aakriticm-slider-3-dot",
			clickable: true,
			renderBullet: function (index, className) {
				return '<span class="' + className + '">' + '<button>' + (index + 1) + '</button>' + "</span>";
			},
		},
	});

	// home 3 beauti
	var slider = new Swiper('.aakriticm-slider-nav-actives', {
		slidesPerView: 1,
		spaceBetween: 30,
		loop: true,
		rtl: rtl_setting,
		effect: 'fade',
		// Navigation arrows
		navigation: {
			nextEl: ".aakriticm-slider-3-button-next",
			prevEl: ".aakriticm-slider-3-button-prev",
		},
		pagination: {
			el: ".aakriticm-slider-3-dot",
			clickable: true,
			renderBullet: function (index, className) {
				return '<span class="' + className + '">' + '<button>' + (index + 1) + '</button>' + "</span>";
			},
		},
	});

	var slider = new Swiper('.aakriticm-product-offer-slider-active', {
		slidesPerView: 4,
		spaceBetween: 30,
		loop: true,
		rtl: rtl_setting,
		pagination: {
			el: ".aakriticm-deals-slider-dot",
			clickable: true,
			renderBullet: function (index, className) {
				return '<span class="' + className + '">' + '<button>' + (index + 1) + '</button>' + "</span>";
			},
		},
		breakpoints: {
			'1200': {
				slidesPerView: 3,
			},
			'992': {
				slidesPerView: 2,
			},
			'768': {
				slidesPerView: 2,
			},
			'576': {
				slidesPerView: 1,
			},
			'0': {
				slidesPerView: 1,
			},
		},
	});

	var slider = new Swiper('.aakriticm-product-arrival-active', {
		slidesPerView: 4,
		spaceBetween: 30,
		loop: true,
		rtl: rtl_setting,
		pagination: {
			el: ".aakriticm-arrival-slider-dot",
			clickable: true,
			renderBullet: function (index, className) {
				return '<span class="' + className + '">' + '<button>' + (index + 1) + '</button>' + "</span>";
			},
		},
		// Navigation arrows
		navigation: {
			nextEl: ".aakriticm-arrival-slider-button-next",
			prevEl: ".aakriticm-arrival-slider-button-prev",
		},
		breakpoints: {
			'1200': {
				slidesPerView: 4,
			},
			'992': {
				slidesPerView: 3,
			},
			'768': {
				slidesPerView: 2,
			},
			'576': {
				slidesPerView: 2,
			},
			'0': {
				slidesPerView: 1,
			},
		},
	});

	var slider = new Swiper('.aakriticm-product-banner-slider-active', {
		slidesPerView: 1,
		spaceBetween: 0,
		loop: true,
		effect: 'fade',
		pagination: {
			el: ".aakriticm-product-banner-slider-dot",
			clickable: true,
			renderBullet: function (index, className) {
				return '<span class="' + className + '">' + '<button>' + (index + 1) + '</button>' + "</span>";
			},
		},

	});

	var slider = new Swiper('.aakriticm-product-gadget-banner-slider-active', {
		slidesPerView: 1,
		spaceBetween: 0,
		loop: true,
		effect: 'fade',
		pagination: {
			el: ".aakriticm-product-gadget-banner-slider-dot",
			clickable: true,
			renderBullet: function (index, className) {
				return '<span class="' + className + '">' + '<button>' + (index + 1) + '</button>' + "</span>";
			},
		},

	});

	var slider = new Swiper('.aakriticm-category-slider-active-2', {
		slidesPerView: 5,
		spaceBetween: 20,
		loop: false,
		rtl: rtl_setting,
		enteredSlides: false,
		pagination: {
			el: ".aakriticm-category-slider-dot",
			clickable: true,
			renderBullet: function (index, className) {
				return '<span class="' + className + '">' + '<button>' + (index + 1) + '</button>' + "</span>";
			},
		},
		// Navigation arrows
		navigation: {
			nextEl: ".aakriticm-category-slider-button-next",
			prevEl: ".aakriticm-category-slider-button-prev",
		},
		scrollbar: {
			el: '.swiper-scrollbar',
			draggable: true,
			dragClass: 'aakriticm-swiper-scrollbar-drag',
			snapOnRelease: true,
		  },
		breakpoints: {
			'1200': {
				slidesPerView: 5,
			},
			'992': {
				slidesPerView: 4,
			},
			'768': {
				slidesPerView: 3,
			},
			'576': {
				slidesPerView: 2,
			},
			'0': {
				slidesPerView: 1,
			},
		},
	});

	var slider = new Swiper('.aakriticm-featured-slider-active', {
		slidesPerView: 3,
		spaceBetween: 10,
		loop: true,
		rtl: rtl_setting,
		enteredSlides: false,
		pagination: {
			el: ".aakriticm-featured-slider-dot",
			clickable: true,
			renderBullet: function (index, className) {
				return '<span class="' + className + '">' + '<button>' + (index + 1) + '</button>' + "</span>";
			},
		},
		// Navigation arrows
		navigation: {
			nextEl: ".aakriticm-featured-slider-button-next",
			prevEl: ".aakriticm-featured-slider-button-prev",
		},

		breakpoints: {
			'1200': {
				slidesPerView: 3,
			},
			'992': {
				slidesPerView: 3,
			},
			'768': {
				slidesPerView: 2,
			},
			'576': {
				slidesPerView: 1,
			},
			'0': {
				slidesPerView: 1,
			},
		},
	});

	var slider = new Swiper('.aakriticm-product-related-slider-active', {
		slidesPerView: 4,
		spaceBetween: 24,
		loop: true,
		rtl: rtl_setting,
		enteredSlides: false,
		pagination: {
			el: ".aakriticm-related-slider-dot",
			clickable: true,
			renderBullet: function (index, className) {
				return '<span class="' + className + '">' + '<button>' + (index + 1) + '</button>' + "</span>";
			},
		},
		// Navigation arrows
		navigation: {
			nextEl: ".aakriticm-related-slider-button-next",
			prevEl: ".aakriticm-related-slider-button-prev",
		},

		scrollbar: {
			el: '.aakriticm-related-swiper-scrollbar',
			draggable: true,
			dragClass: 'aakriticm-swiper-scrollbar-drag',
			snapOnRelease: true,
		  },

		breakpoints: {
			'1200': {
				slidesPerView: 4,
			},
			'992': {
				slidesPerView: 3,
			},
			'768': {
				slidesPerView: 2,
			},
			'576': {
				slidesPerView: 2,
			},
			'0': {
				slidesPerView: 1,
			},
		},
	});

	var slider = new Swiper('.aakriticm-testimoinal-slider-active-3', {
		slidesPerView: 2,
		spaceBetween: 24,
		loop: true,
		rtl: rtl_setting,
		enteredSlides: false,
		pagination: {
			el: ".aakriticm-testimoinal-slider-dot-3",
			clickable: true,
			renderBullet: function (index, className) {
				return '<span class="' + className + '">' + '<button>' + (index + 1) + '</button>' + "</span>";
			},
		},
		// Navigation arrows
		navigation: {
			nextEl: ".aakriticm-testimoinal-slider-button-next-3",
			prevEl: ".aakriticm-testimoinal-slider-button-prev-3",
		},

		breakpoints: {
			'1200': {
				slidesPerView: 2,
			},
			'992': {
				slidesPerView: 2,
			},
			'768': {
				slidesPerView: 1,
			},
			'576': {
				slidesPerView: 1,
			},
			'0': {
				slidesPerView: 1,
			},
		},
	});

	var slider = new Swiper('.aakriticm-category-slider-active-4', {
		slidesPerView: 5,
		spaceBetween: 25,
		loop: true,
		rtl: rtl_setting,
		enteredSlides: false,
		pagination: {
			el: ".aakriticm-category-slider-dot-4",
			clickable: true,
			renderBullet: function (index, className) {
				return '<span class="' + className + '">' + '<button>' + (index + 1) + '</button>' + "</span>";
			},
		},
		// Navigation arrows
		navigation: {
			nextEl: ".aakriticm-category-slider-button-next-4",
			prevEl: ".aakriticm-category-slider-button-prev-4",
		},

		scrollbar: {
			el: '.aakriticm-category-swiper-scrollbar',
			draggable: true,
			dragClass: 'aakriticm-swiper-scrollbar-drag',
			snapOnRelease: true,
		  },

		breakpoints: {
			'1400': {
				slidesPerView: 5,
			},
			'1200': {
				slidesPerView: 4,
			},
			'992': {
				slidesPerView: 3,
			},
			'768': {
				slidesPerView: 2,
			},
			'576': {
				slidesPerView: 2,
			},
			'0': {
				slidesPerView: 1,
			},
		},
	});

	var slider = new Swiper('.aakriticm-category-slider-active-5', {
		slidesPerView: 6,
		spaceBetween: 12,
		loop: true,
		rtl: rtl_setting,
		enteredSlides: false,
		pagination: {
			el: ".aakriticm-category-slider-dot-4",
			clickable: true,
			renderBullet: function (index, className) {
				return '<span class="' + className + '">' + '<button>' + (index + 1) + '</button>' + "</span>";
			},
		},
		// Navigation arrows
		navigation: {
			nextEl: ".aakriticm-category-slider-button-next-5",
			prevEl: ".aakriticm-category-slider-button-prev-5",
		},

		scrollbar: {
			el: '.aakriticm-category-5-swiper-scrollbar',
			draggable: true,
			dragClass: 'aakriticm-swiper-scrollbar-drag',
			snapOnRelease: true,
		  },

		breakpoints: {
			'1400': {
				slidesPerView: 6,
			},
			'1200': {
				slidesPerView: 5,
			},
			'992': {
				slidesPerView: 4,
			},
			'768': {
				slidesPerView: 3,
			},
			'576': {
				slidesPerView: 2,
			},
			'400': {
				slidesPerView: 2,
			},
			'0': {
				slidesPerView: 1,
			},
		},
	});

	var slider = new Swiper('.aakriticm-brand-slider-active', {
		slidesPerView: 5,
		spaceBetween: 0,
		loop: true,
		rtl: rtl_setting,
		enteredSlides: false,
		pagination: {
			el: ".aakriticm-brand-slider-dot",
			clickable: true,
			renderBullet: function (index, className) {
				return '<span class="' + className + '">' + '<button>' + (index + 1) + '</button>' + "</span>";
			},
		},
		// Navigation arrows
		navigation: {
			nextEl: ".aakriticm-brand-slider-button-next",
			prevEl: ".aakriticm-brand-slider-button-prev",
		},

		breakpoints: {
			'1200': {
				slidesPerView: 5,
			},
			'992': {
				slidesPerView: 5,
			},
			'768': {
				slidesPerView: 4,
			},
			'576': {
				slidesPerView: 3,
			},
			'0': {
				slidesPerView: 1,
			},
		},
	});

	var slider = new Swiper('.aakriticm-best-slider-active', {
		slidesPerView: 4,
		spaceBetween: 24,
		loop: true,
		rtl: rtl_setting,
		enteredSlides: false,
		pagination: {
			el: ".aakriticm-best-slider-dot",
			clickable: true,
			renderBullet: function (index, className) {
				return '<span class="' + className + '">' + '<button>' + (index + 1) + '</button>' + "</span>";
			},
		},
		// Navigation arrows
		navigation: {
			nextEl: ".aakriticm-best-slider-button-next",
			prevEl: ".aakriticm-best-slider-button-prev",
		},

		scrollbar: {
			el: '.aakriticm-best-swiper-scrollbar',
			draggable: true,
			dragClass: 'aakriticm-swiper-scrollbar-drag',
			snapOnRelease: true,
		  },

		breakpoints: {
			'1200': {
				slidesPerView: 4,
			},
			'992': {
				slidesPerView: 4,
			},
			'768': {
				slidesPerView: 2,
			},
			'576': {
				slidesPerView: 2,
			},
			'0': {
				slidesPerView: 1,
			},
		},
	});

	var slider = new Swiper('.aakriticm-best-slider-active-5', {
		slidesPerView: 3,
		spaceBetween: 24,
		loop: true,
		rtl: rtl_setting,
		enteredSlides: false,
		pagination: {
			el: ".aakriticm-best-slider-dot-5",
			clickable: true,
			renderBullet: function (index, className) {
				return '<span class="' + className + '">' + '<button>' + (index + 1) + '</button>' + "</span>";
			},
		},
		// Navigation arrows
		navigation: {
			nextEl: ".aakriticm-best-slider-5-button-next",
			prevEl: ".aakriticm-best-slider-5-button-prev",
		},

		scrollbar: {
			el: '.aakriticm-best-5-swiper-scrollbar',
			draggable: true,
			dragClass: 'aakriticm-swiper-scrollbar-drag',
			snapOnRelease: true,
		  },

		breakpoints: {
			'1200': {
				slidesPerView: 3,
			},
			'992': {
				slidesPerView: 2,
			},
			'768': {
				slidesPerView: 2,
			},
			'576': {
				slidesPerView: 2,
			},
			'0': {
				slidesPerView: 1,
			},
		},
	});

	var slider = new Swiper('.aakriticm-product-details-thumb-slider-active', {
		slidesPerView: 2,
		spaceBetween: 13,
		loop: true,
		rtl: rtl_setting,
		enteredSlides: false,
		pagination: {
			el: ".aakriticm-product-details-thumb-slider-dot",
			clickable: true,
			renderBullet: function (index, className) {
				return '<span class="' + className + '">' + '<button>' + (index + 1) + '</button>' + "</span>";
			},
		},
		// Navigation arrows
		navigation: {
			nextEl: ".aakriticm-product-details-thumb-slider-5-button-next",
			prevEl: ".aakriticm-product-details-thumb-slider-5-button-prev",
		},


		breakpoints: {
			'1200': {
				slidesPerView: 2,
			},
			'992': {
				slidesPerView: 2,
			},
			'768': {
				slidesPerView: 2,
			},
			'576': {
				slidesPerView: 2,
			},
			'0': {
				slidesPerView: 1,
			},
		},
	});

	var slider = new Swiper('.aakriticm-trending-slider-active', {
		slidesPerView: 2,
		spaceBetween: 24,
		loop: true,
		rtl: rtl_setting,
		enteredSlides: false,
		pagination: {
			el: ".aakriticm-trending-slider-dot",
			clickable: true,
			renderBullet: function (index, className) {
				return '<span class="' + className + '">' + '<button>' + (index + 1) + '</button>' + "</span>";
			},
		},
		// Navigation arrows
		navigation: {
			nextEl: ".aakriticm-trending-slider-button-next",
			prevEl: ".aakriticm-trending-slider-button-prev",
		},

		breakpoints: {
			'1200': {
				slidesPerView: 2,
			},
			'992': {
				slidesPerView: 2,
			},
			'768': {
				slidesPerView: 2,
			},
			'576': {
				slidesPerView: 2,
			},
			'0': {
				slidesPerView: 1,
			},
		},
	});

	var specialSlider = new Swiper('.aakriticm-special-slider-active', {
		slidesPerView: 1,
		spaceBetween: 0,
		loop: true,
		rtl: rtl_setting,
		effect: 'fade',
		enteredSlides: false,
		pagination: {
			el: ".aakriticm-special-slider-dot",
			clickable: true,
			renderBullet: function (index, className) {
				return '<span class="' + className + '">' + '<button>' + (index + 1) + '</button>' + "</span>";
			},
		},
		// Navigation arrows
		navigation: {
			nextEl: ".aakriticm-special-slider-button-next",
			prevEl: ".aakriticm-special-slider-button-prev",
		},
	});

	var slider = new Swiper('.aakriticm-testimonial-slider-active', {
		slidesPerView: 1,
		spaceBetween: 0,
		loop: true,
		rtl: rtl_setting,
		pagination: {
			el: ".aakriticm-testimonial-slider-dot",
			clickable: true,
			renderBullet: function (index, className) {
				return '<span class="' + className + '">' + '<button>' + (index + 1) + '</button>' + "</span>";
			},
		},
		// Navigation arrows
		navigation: {
			nextEl: ".aakriticm-testimonial-slider-button-next",
			prevEl: ".aakriticm-testimonial-slider-button-prev",
		},
	});

	var slider = new Swiper('.aakriticm-testimonial-slider-active-5', {
		slidesPerView: 1,
		spaceBetween: 0,
		loop: true,
		rtl: rtl_setting,
		enteredSlides: false,
		pagination: {
			el: ".aakriticm-testimonial-slider-dot-5",
			clickable: true,
			renderBullet: function (index, className) {
				return '<span class="' + className + '">' + '<button>' + (index + 1) + '</button>' + "</span>";
			},
		},
		// Navigation arrows
		navigation: {
			nextEl: ".aakriticm-testimonial-slider-5-button-next",
			prevEl: ".aakriticm-testimonial-slider-5-button-prev",
		},
		
	});

	var slider = new Swiper('.aakriticm-best-banner-slider-active-5', {
		slidesPerView: 1,
		spaceBetween: 0,
		loop: true,
		rtl: rtl_setting,
		enteredSlides: false,
		effect : 'fade',
		pagination: {
			el: ".aakriticm-best-banner-slider-dot-5",
			clickable: true,
			renderBullet: function (index, className) {
				return '<span class="' + className + '">' + '<button>' + (index + 1) + '</button>' + "</span>";
			},
		},
		// Navigation arrows
		navigation: {
			nextEl: ".aakriticm-best-banner-slider-5-button-next",
			prevEl: ".aakriticm-best-banner-slider-5-button-prev",
		},
	});

	var postboxSlider = new Swiper('.aakriticm-postbox-slider', {
		slidesPerView: 1,
		spaceBetween: 0,
		loop: true,
		rtl: rtl_setting,
		autoplay: {
			delay: 3000,
		},
		// Navigation arrows
		navigation: {
			nextEl: ".aakriticm-postbox-slider-button-next",
			prevEl: ".aakriticm-postbox-slider-button-prev",
		},
		breakpoints: {
			'1200': {
				slidesPerView: 1,
			},
			'992': {
				slidesPerView: 1,
			},
			'768': {
				slidesPerView: 1,
			},
			'576': {
				slidesPerView: 1,
			},
			'0': {
				slidesPerView: 1,
			},
		},
	});

	var historyNav = new Swiper(".aakriticm-history-nav-active", {
		spaceBetween: 220,
		slidesPerView: 4,
		watchSlidesProgress: true,
	  });
	  var historyMain = new Swiper(".aakriticm-history-slider-active", {
		spaceBetween: 0,
		effect : 'fade',
		navigation: {
		  nextEl: ".swiper-button-next",
		  prevEl: ".swiper-button-prev",
		},
		thumbs: {
		  swiper: historyNav,
		},
	  });


	////////////////////////////////////////////////////
	// 15. Masonary Js
	$('.grid').imagesLoaded(function () {
		// init Isotope
		var $grid = $('.grid').isotope({
			itemSelector: '.grid-item',
			percentPosition: true,
			masonry: {
				// use outer width of grid-sizer for columnWidth
				columnWidth: '.grid-item',
			}
		});


		// filter items on button click
		$('.masonary-menu').on('click', 'button', function () {
			var filterValue = $(this).attr('data-filter');
			$grid.isotope({ filter: filterValue });
		});

		//for menu active class
		$('.masonary-menu button').on('click', function (event) {
			$(this).siblings('.active').removeClass('active');
			$(this).addClass('active');
			event.preventDefault();
		});

	});

	/* magnificPopup img view */
	$('.popup-image').magnificPopup({
		type: 'image',
		gallery: {
			enabled: true
		}
	});

	/* magnificPopup video view */
	$(".popup-video").magnificPopup({
		type: "iframe",
	});


	if ($('.scene').length > 0) {
		$('.scene').parallax({
			scalarX: 5.0,
			scalarY: 5.0,
		});
	};

	////////////////////////////////////////////////////
	// 16. Wow Js
	new WOW().init();

	function tp_ecommerce() {
		$('.aakriticm-cart-minus').on('click', function () {
			var $input = $(this).parent().find('input');
			var count = parseInt($input.val()) - 1;
			count = count < 1 ? 1 : count;
			$input.val(count);
			$input.change();
			return false;
		});
	
		$('.aakriticm-cart-plus').on('click', function () {
			var $input = $(this).parent().find('input');
			$input.val(parseInt($input.val()) + 1);
			$input.change();
			return false;
		});

		$("#slider-range").slider({
			range: true,
			min: 0,
			max: 500,
			values: [75, 300],
			slide: function (event, ui) {
				$("#amount").val("$" + ui.values[0] + " - $" + ui.values[1]);
			}
		});
		$("#amount").val("$" + $("#slider-range").slider("values", 0) +
			" - $" + $("#slider-range").slider("values", 1));

		$("#slider-range-offcanvas").slider({
			range: true,
			min: 0,
			max: 500,
			values: [75, 300],
			slide: function (event, ui) {
				$("#amount-offcanvas").val("$" + ui.values[0] + " - $" + ui.values[1]);
			}
		});
		$("#amount-offcanvas").val("$" + $("#slider-range-offcanvas").slider("values", 0) +
			" - $" + $("#slider-range-offcanvas").slider("values", 1));
	
		

		$('.aakriticm-checkout-payment-item label').on('click', function () {
			$(this).siblings('.aakriticm-checkout-payment-desc').slideToggle(400);
			
		});
		

		$('.aakriticm-color-variation-btn').on('click', function () {
			$(this).addClass('active').siblings().removeClass('active');
		});
		

		$('.aakriticm-size-variation-btn').on('click', function () {
			$(this).addClass('active').siblings().removeClass('active');
		});
	
		////////////////////////////////////////////////////
		// 17. Show Login Toggle Js
		$('.aakriticm-checkout-login-form-reveal-btn').on('click', function () {
			$('#tpReturnCustomerLoginForm').slideToggle(400);
		});
	
		////////////////////////////////////////////////////
		// 18. Show Coupon Toggle Js
		$('.aakriticm-checkout-coupon-form-reveal-btn').on('click', function () {
			$('#tpCheckoutCouponForm').slideToggle(400);
		});
	
		////////////////////////////////////////////////////
		// 19. Create An Account Toggle Js
		$('#cbox').on('click', function () {
			$('#cbox_info').slideToggle(900);
		});
	
		////////////////////////////////////////////////////
		// 20. Shipping Box Toggle Js
		$('#ship-box').on('click', function () {
			$('#ship-box-info').slideToggle(1000);
		});

		$("#slider-range").slider({
			range: true,
			min: 0,
			max: 500,
			values: [75, 300],
			slide: function (event, ui) {
			  $("#amount").val("$" + ui.values[0] + " - $" + ui.values[1]);
			},
		});
	}
	tp_ecommerce();

	

	////////////////////////////////////////////////////
	// 17. Counter Js
	new PureCounter();
	new PureCounter({
		filesizing: true,
		selector: ".filesizecount",
		pulse: 2,
	});

	////////////////////////////////////////////////////
	// 18. InHover Active Js
	$('.hover__active').on('mouseenter', function () {
		$(this).addClass('active').parent().siblings().find('.hover__active').removeClass('active');
	});

	$('.activebsba').on("click", function () {
		$('#services-item-thumb').removeClass().addClass($(this).attr('rel'));
		$(this).addClass('active').siblings().removeClass('active');
	});


	////////////////////////////////////////////////////
	// 19. Line Animation Js
	if ($('#marker').length > 0) {
		function tp_tab_line(){
			var marker = document.querySelector('#marker');
			var item = document.querySelectorAll('.menu-style-3  > nav > ul > li');
			var itemActive = document.querySelector('.menu-style-3  > nav > ul > li.active');

			function indicator(e){
				marker.style.left = e.offsetLeft+"px";
				marker.style.width = e.offsetWidth+"px";
			}
				
		
			item.forEach(link => {
				link.addEventListener('mouseenter', (e)=>{
					indicator(e.target);
				});
				
			});

			
			var activeNav = $('.menu-style-3 > nav > ul > li.active');
			var activewidth = $(activeNav).width();
			var activePadLeft = parseFloat($(activeNav).css('padding-left'));
			var activePadRight = parseFloat($(activeNav).css('padding-right'));
			var totalWidth = activewidth + activePadLeft + activePadRight;
			
			var precedingAnchorWidth = anchorWidthCounter();
		
		
			$(marker).css('display','block');
			
			$(marker).css('width', totalWidth);
		
			function anchorWidthCounter() {
				var anchorWidths = 0;
				var a;
				var aWidth;
				var aPadLeft;
				var aPadRight;
				var aTotalWidth;
				$('.menu-style-3 > nav > ul > li').each(function(index, elem) {
					var activeTest = $(elem).hasClass('active');
					marker.style.left = elem.offsetLeft+"px";
					if(activeTest) {
					// Break out of the each function.
					return false;
					}
			
					a = $(elem).find('li');
					aWidth = a.width();
					aPadLeft = parseFloat(a.css('padding-left'));
					aPadRight = parseFloat(a.css('padding-right'));
					aTotalWidth = aWidth + aPadLeft + aPadRight;
			
					anchorWidths = anchorWidths + aTotalWidth;
	
				});
		
				return anchorWidths;
			}
		}
		tp_tab_line();
	}


	if ($('#productTabMarker').length > 0) {
		function tp_tab_line_2(){
			var marker = document.querySelector('#productTabMarker');
			var item = document.querySelectorAll('.aakriticm-product-tab button');
			var itemActive = document.querySelector('.aakriticm-product-tab .nav-link.active');

			// rtl settings
			var tp_rtl = localStorage.getItem('tp_dir');
			let rtl_setting = tp_rtl == 'rtl' ? 'right' : 'left';

			function indicator(e){
				marker.style.left = e.offsetLeft+"px";
				marker.style.width = e.offsetWidth+"px";
			}
				
		
			item.forEach(link => {
				link.addEventListener('click', (e)=>{
					indicator(e.target);
				});
			});
			
			var activeNav = $('.nav-link.active');
			var activewidth = $(activeNav).width();
			var activePadLeft = parseFloat($(activeNav).css('padding-left'));
			var activePadRight = parseFloat($(activeNav).css('padding-right'));
			var totalWidth = activewidth + activePadLeft + activePadRight;
			
			var precedingAnchorWidth = anchorWidthCounter();
		
		
			$(marker).css('display','block');
			
			$(marker).css('width', totalWidth);
		
			function anchorWidthCounter() {
				var anchorWidths = 0;
				var a;
				var aWidth;
				var aPadLeft;
				var aPadRight;
				var aTotalWidth;
				$('.aakriticm-product-tab button').each(function(index, elem) {
					var activeTest = $(elem).hasClass('active');
					marker.style.left = elem.offsetLeft+"px";
					if(activeTest) {
					// Break out of the each function.
					return false;
					}
			
					a = $(elem).find('button');
					aWidth = a.width();
					aPadLeft = parseFloat(a.css('padding-left'));
					aPadRight = parseFloat(a.css('padding-right'));
					aTotalWidth = aWidth + aPadLeft + aPadRight;
			
					anchorWidths = anchorWidths + aTotalWidth;
	
				});
		
				return anchorWidths;
			}
		}
		tp_tab_line_2();
	}

	////////////////////////////////////////////////////
	// 20. Video Play Js
	var play = false;
	$('.aakriticm-video-toggle-btn').on('click', function(){

		if(play === false){
			$('.aakriticm-slider-video').addClass('full-width');
			$(this).addClass('hide');
			play = true;

			$('.aakriticm-slider-video').find('video').each(function() {
				$(this).get(0).play();
			});
		}else{
			$('.aakriticm-slider-video').removeClass('full-width');
			$(this).removeClass('hide');
			play = false;
			$('.aakriticm-slider-video').find('video').each(function() {
				$(this).get(0).pause();
			});
		}

	});

	////////////////////////////////////////////////////
	// 21. Password Toggle Js
	if($('#password-show-toggle').length > 0){
		var btn = document.getElementById('password-show-toggle');
		
		btn.addEventListener('click', function(e){
			
			var inputType = document.getElementById('tp_password');
			var openEye = document.getElementById('open-eye');
			var closeEye = document.getElementById('close-eye');
	
			if (inputType.type === "password") {
				inputType.type = "text";
				openEye.style.display = 'block';
				closeEye.style.display = 'none';
			 } else {
				inputType.type = "password";
				openEye.style.display = 'none';
				closeEye.style.display = 'block';
			 }
		});
	}

	
	if ($('.aakriticm-header-height').length > 0) {
		var headerHeight = document.querySelector(".aakriticm-header-height");      
		var setHeaderHeight = headerHeight.offsetHeight;	
		
		$(".aakriticm-header-height").each(function () {
			$(this).css({
				'height' : setHeaderHeight + 'px'
			});
		});
	  }

	if ($('.infinite-container').length > 0) {
		let ias = new InfiniteAjaxScroll('.infinite-container', {
			item: '.infinite-item',
			next: '.infinite-next-link',
			pagination: '.infinite-pagination'
		});

	}

	if ($('.load-more-content').length > 0) {
		$('.load-more-content').btnLoadmore({
			showItem : 9,
			whenClickBtn : 3,
			textBtn : 'Load More Products',
			classBtn : 'aakriticm-btn aakriticm-btn-border aakriticm-btn-border-primary'
		});
	}

})(jQuery);